import argparse

from flask import Flask, request, jsonify, render_template, send_file, flash
import torch
# import numpy as np
# import os
# from torchvision import transforms
# from models.experimental import attempt_load
# #from utils.plots import plot_one_box
import os
import cv2
import detect_s
import segment_s
import class_s
import train
import val
import detect
from detect_s import run, main
from train import run, main
from val import run, main
from detect import run, main
from segment_s import main
from class_s import main
# from detect import run, main
from flask_cors import *
import json

import zipfile
import glob
from PIL import Image
import shutil
import base64
from zipfile import ZipFile

app = Flask(__name__)

@app.route('/save')
def save():
    CORS(app, supports_credentials=True)
    # 指定文件夹路径
    # if request.method == 'POST':
    # file_paths = {}
    file_paths = []
    file_path = "./runs/train/"
    files = os.listdir(file_path)
    i = 0
    for file in files:
        src = os.path.join(file_path, file+'/weights/best.pt')
        # print(src)
        if os.path.isfile(src):
            file_paths.append(src)
            # file_paths[i] = src
            # i += 1
    # 返回文件下载页面
    # return file_paths
    print(file_paths)
    return render_template('index_download.html', file_paths=file_paths)

@app.route('/download/<path:filename>')
def download_file(filename):
    CORS(app, supports_credentials=True)
    # 获取文件路径
    file_path = filename
    # 提供文件下载
    return send_file(file_path, as_attachment=True)


# 加载数据保存到路径 读取文件夹中的文件，所有图像处理成200*200的像素进行保存，标签也 保存到datasets/NEU/ images和labels
@app.route('/updata', methods=['GET', 'POST'])
def upload_updata():
    CORS(app, supports_credentials=True)
    if request.method == 'POST':  #post是一种请求方式
        # 从表单中获取上传的压缩文件
        file = request.files['zip']  #request.files 函数作用就是获取前端名为 'file'的文件信息
        # 保存上传的压缩文件
        zip_path = './datasets/temp/file_zip.zip'

        if os.path.exists(zip_path):
            # return json.dumps("updata_success")
            os.remove(zip_path)
        if os.path.exists('./datasets/temp/file_zip/'):
            # return json.dumps("updata_success")
            shutil.rmtree('./datasets/temp/file_zip/')

        file.save(zip_path)
        # 解压缩乱码问题
        def support_gbk(zip_file: ZipFile):
            name_to_info = zip_file.NameToInfo
            # copy map first
            for name, info in name_to_info.copy().items():
                real_name = name.encode('cp437').decode('gbk')
                if real_name != name:
                    info.filename = real_name
                    del name_to_info[name]
                    name_to_info[real_name] = info
            return zip_file
        # 解压缩文件
        extract_folder = './datasets/temp/file_zip'
        with support_gbk(ZipFile(zip_path, 'r')) as zip_ref:
            zip_ref.extractall(extract_folder)
        train_images_zip = extract_folder + '/train/images/'
        train_labels_zip = extract_folder + '/train/labels/'
        val_images_zip = extract_folder + '/val/images/'
        val_labels_zip = extract_folder + '/val/labels/'
        train_images = './datasets/data/train/images/'
        train_labels = './datasets/data/train/labels/'
        val_images = './datasets/data/val/images/'
        val_labels = './datasets/data/val/labels/'

        # 判断是否存在，存在则删除
        if os.path.exists('./datasets/data/train/'):
            # return json.dumps("updata_success")
            shutil.rmtree('./datasets/data/train/')
        if os.path.exists('./datasets/data/val/'):
            # return json.dumps("updata_success")
            shutil.rmtree('./datasets/data/val/')

        # 保存文件到路径data
        shutil.copytree(train_images_zip, train_images)
        shutil.copytree(train_labels_zip, train_labels)
        shutil.copytree(val_images_zip, val_images)
        shutil.copytree(val_labels_zip, val_labels)

        # return json.dumps("updata_success")
        return render_template('index_updata.html')

    return render_template('index_updata.html')

@app.route('/pretreatment', methods=['GET', 'POST'])
def upload_pretreatment():
    CORS(app, supports_credentials=True)
    if request.method == 'POST':  #post是一种请求方式

        train_images = './datasets/data/train/images/'
        val_images = './datasets/data/val/images/'

        for img in os.listdir(train_images):
            # 不同格式
            if (img.endswith('.gif') or img.endswith('.png') or img.endswith('.jpg') or img.endswith('.JPG')):
                # 修改图片，存储图片
                oldimg = Image.open(train_images + img)
                # 大小缩放为64*64
                new_img = oldimg.resize((320, 240))
                # 以原名称存储图片
                new_img.save(train_images + img)

        for img in os.listdir(val_images):
            # 不同格式
            if (img.endswith('.gif') or img.endswith('.png') or img.endswith('.jpg') or img.endswith('.JPG')):
                oldimg = Image.open(val_images + img)
                new_img = oldimg.resize((320, 240))
                # new_img = oldimg
                new_img.save(val_images + img)

        # return json.dumps("pretreatment_success")
        return render_template('index_pretreatment.html')

    return render_template('index_pretreatment.html')

# 训练
@app.route('/train', methods=['GET', 'POST'])
def upload_train():
    CORS(app, supports_credentials=True)
    if request.method == 'POST':  #post是一种请求方式
        opt = train.parse_opt()
        print(json.dumps("start"))
        train.main(opt)
        print(json.dumps("success"))

        # return json.dumps("train_success")
        return render_template('index_train.html')

    return render_template('index_train.html')
    # return


# 验证
@app.route('/val', methods=['GET', 'POST'])
def upload_val():
    CORS(app, supports_credentials=True)
    if request.method == 'POST':  #post是一种请求方式
        opt = val.parse_opt()
        print(json.dumps("start"))
        val.main(opt)
        print(json.dumps("success"))
        # 返回验证结果

        # 查找最新出现的val exp文件
        # path = './runs/val'
        # lists = os.listdir(path)
        # lists.sort(key=lambda x: os.path.getmtime((path + "\\" + x)))
        # file_new = os.path.join(path, lists[-1])
        # print(file_new)
        file_new = './runs/val/exp2'

        confusion_matrix = return_img_stream(file_new + '/confusion_matrix.png')
        F1_curve = return_img_stream(file_new + '/F1_curve.png')
        P_curve = return_img_stream(file_new + '/P_curve.png')
        R_curve = return_img_stream(file_new + '/R_curve.png')
        PR_curve = return_img_stream(file_new + '/PR_curve.png')

        # result_text文件读出来str输出
        f = open(file_new+'/result_text1.txt', "r")
        lines = f.readlines()
        result_text = ''
        for line in lines:
            result_text += line
        print(result_text)

        List={}
        List[0]=confusion_matrix
        List[1]=F1_curve
        List[2]=P_curve
        List[3]=R_curve
        List[4]=PR_curve
        List[5]=result_text
        # Lists={
        #     ['confusion_matrix',confusion_matrix],
        #        ['F1_curve',F1_curve],
        #        ['P_curve',P_curve],
        #        ['R_curve',R_curve],
        #        ['PR_curve',PR_curve],
        #        ['result_text',result_text]
        #        }
        # return List
        return render_template('index_val.html', confusion_matrix=confusion_matrix, F1_curve=F1_curve, P_curve=P_curve, R_curve=R_curve, PR_curve=PR_curve, result_text=json.dumps(result_text))
        # return json.dumps(confusion_matrix),json.dumps(F1_curve),json.dumps(P_curve),json.dumps(R_curve),json.dumps(PR_curve),json.dumps(result_text)
        # return json.dumps("val_success")

    return render_template('index_val.html')
    # return


@app.route('/detect', methods=['GET', 'POST'])
def upload_detect():
    CORS(app, supports_credentials=True)
    if request.method == 'POST':  # post是一种请求方式
        opt = detect.parse_opt()
        print(json.dumps("start"))
        detect.main(opt)
        print(json.dumps("success"))

        detect_stream = []

        path_origin = './datasets/data/val/images'
        for filename in os.listdir(path_origin):
            img_stream = return_img_stream(path_origin + "/" + filename)
            detect_stream.append(img_stream)

        path_detect = './runs/detect'
        lists = os.listdir(path_detect)
        lists.sort(key=lambda x: os.path.getmtime((path_detect + "\\" + x)))
        file_new = os.path.join(path_detect, lists[-1])
        print(file_new)

        for filename in os.listdir(file_new):
            img_stream = return_img_stream(file_new + "/" + filename)
            detect_stream.append(img_stream)
        # print(detect_stream)

        # return json.dumps(detect_stream)
        # return render_template('index_detect.html', result_text=json.dumps(detect_stream))
        return json.dumps("detect_success")
    return render_template('index_detect.html')


# 测试单张图像
@app.route('/class_s', methods=['GET', 'POST'])
def upload_class_s():
    CORS(app, supports_credentials=True)
    if request.method == 'POST':  #post是一种请求方式
        # 从表单中获取上传的文件
        f = request.files['edu_image']  #request.files 函数作用就是获取前端名为 'file'的文件信息
        if f:
            global filename  # 定义全局变量，方便其他地方调用filename，如果不定义全局变量，其他地方无法调用
            filename = f.filename  # 获取前端上传图片名字
            global file_path  #同理，定义全局变量

            # 将文件保存到服务器本地
            file_path = os.path.join(os.getcwd(), filename)  #本地路径+图片名字= 文件路径（file-path)

            print(file_path)  # 当时只是为了测试程序
            f.save(file_path)  # 保存上传的图片到本地目录下，方便后续推理，直接找到图片 file_path是保存原图的路径
            # 返回文件路径
            origin = return_img_stream(file_path)
            #进行检测
            result = class_s.main(file_path)
            List = {}
            List[result] = origin
            print(result)
            # return List
            return render_template('index_class_s.html', origin=origin, result=result)

    return render_template('index_class_s.html')

# 测试单张图像
@app.route('/seg_s', methods=['GET', 'POST'])
def upload_seg_s():
    CORS(app, supports_credentials=True)
    if request.method == 'POST':  #post是一种请求方式
        # 从表单中获取上传的文件
        f = request.files['edu_image']  #request.files 函数作用就是获取前端名为 'file'的文件信息
        if f:
            global filename  # 定义全局变量，方便其他地方调用filename，如果不定义全局变量，其他地方无法调用
            filename = f.filename  # 获取前端上传图片名字
            global file_path  #同理，定义全局变量

            # 将文件保存到服务器本地
            file_path = os.path.join(os.getcwd(), filename)  #本地路径+图片名字= 文件路径（file-path)

            print(file_path)  # 当时只是为了测试程序
            f.save(file_path)  # 保存上传的图片到本地目录下，方便后续推理，直接找到图片 file_path是保存原图的路径
            # 返回文件路径
            origin = return_img_stream(file_path)

            #进行检测
            segment_s.main(file_path, filename)
            # 图片路径，推理完之后，默认保存的就是runs\\detect\\exp，这里加上filename，是变成完整的图片路径，然后才能获取显示
            img_path = 'run\\segment\\exp\\' + str(filename).split(".")[0]+'.png'

            # img_path
            # 画线
            img = cv2.imread(file_path)
            mask = cv2.imread(img_path)
            mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
            ret, thresh = cv2.threshold(mask, 255, 255, 255)
            contours, im = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # 第一个参数是轮廓
            cv2.drawContours(image=img, contours=contours, contourIdx=-1, color=(255, 255, 255), thickness=2)
            cv2.imwrite('run\\segment\\exp\\' + str(filename).split(".")[0] + '.png', img)  # 将img写入到

            # mask.save()

            result = return_img_stream(img_path)  # 获取图片流
            List = {}
            List[0] = origin
            List[1] = result

            # return json.dumps(result)
            # return List
            return render_template('index_seg_s.html', origin=origin, result=result)

    return render_template('index_seg_s.html')

# # 测试单张图像
# @app.route('/seg_s', methods=['GET', 'POST'])
# def upload_seg_s():
#     CORS(app, supports_credentials=True)
#     if request.method == 'POST':  #post是一种请求方式
#         # 从表单中获取上传的文件
#         f = request.files['edu_image']  #request.files 函数作用就是获取前端名为 'file'的文件信息
#         if f:
#             global filename  # 定义全局变量，方便其他地方调用filename，如果不定义全局变量，其他地方无法调用
#             filename = f.filename  # 获取前端上传图片名字
#             global file_path  #同理，定义全局变量
#
#             # 将文件保存到服务器本地
#             file_path = os.path.join(os.getcwd(), filename)  #本地路径+图片名字= 文件路径（file-path)
#
#             f.save(file_path)  # 保存上传的图片到本地目录下，方便后续推理，直接找到图片 file_path是保存原图的路径
#             # 返回文件路径
#             origin = return_img_stream(file_path)
#
#             #进行检测
#             # detect_seg_s.main(file_path, filename)
#             # 图片路径，推理完之后，默认保存的就是runs\\detect\\exp，这里加上filename，是变成完整的图片路径，然后才能获取显示
#             img_path = './datasets/seg_result/' + str(filename)
#             result = return_img_stream(img_path)  # 获取图片流
#             List = {}
#             List[0] = origin
#             List[1] = result
#
#             return List
#             # return render_template('index_seg_s.html', origin=origin, result=result)
#
#     return render_template('index_seg_s.html')


# # 测试单张图像
@app.route('/', methods=['GET', 'POST'])
def upload():
    CORS(app, supports_credentials=True)
    if request.method == 'POST':  #post是一种请求方式
        # 从表单中获取上传的文件
        f = request.files['edu_image']  #request.files 函数作用就是获取前端名为 'file'的文件信息
        if f:
            global filename  # 定义全局变量，方便其他地方调用filename，如果不定义全局变量，其他地方无法调用
            filename = f.filename  # 获取前端上传图片名字
            global file_path  #同理，定义全局变量

            # 将文件保存到服务器本地
            file_path = os.path.join(os.getcwd(), filename)  #本地路径+图片名字= 文件路径（file-path)

            print(file_path)  # 当时只是为了测试程序
            f.save(file_path)  # 保存上传的图片到本地目录下，方便后续推理，直接找到图片 file_path是保存原图的路径
            # 返回文件路径
            origin = return_img_stream(file_path)
            # print(origin)
            # return file_path

            #进行检测
            opt = parse_opt_s()
            detect_s.main(opt)
            # 图片路径，推理完之后，默认保存的就是run\\detect\\exp，这里加上filename，是变成完整的图片路径，然后才能获取显示
            img_path = 'run\\detect\\exp\\' + str(filename)
            result = return_img_stream(img_path)  # 获取图片流
            # print(result)
            # print(type(result))

            List = {}
            List[0] = origin
            List[1] = result

            # return json.dumps(result)
            # return List
            return render_template('index_detect_s.html', origin=origin, result=result)

    return render_template('index_detect_s.html')


# 检测结果显示
def return_img_stream(img_local_path):
    """
    工具函数:
    获取本地图片流
    :param img_local_path:文件单张图片的本地绝对路径
    :return: 图片流
    """
    import base64
    img_stream = ''
    with open(img_local_path, 'rb') as img_f:
        img_stream = img_f.read()
        img_stream = base64.b64encode(img_stream).decode()
    return img_stream

# @app.route('/sh', methods=['GET', 'POST'])  #定义新路由，显示图片
# def hello_world():

def parse_opt_s():
    parser = argparse.ArgumentParser()

    # parser.add_argument('--weights', nargs='+', type=str, default= 'yolov5s.pt', help='model path or triton URL')
    parser.add_argument('--weights', nargs='+', type=str, default='best.pt', help='model path or triton URL')
    # parser.add_argument('--source', type=str, default=0, help='file/dir/URL/glob/screen/0(webcam)')
    parser.add_argument('--source', type=str, default=file_path, help='file/dir/URL/glob/screen/0(webcam)')

    parser.add_argument('--data', type=str, default='edu/edu_parameter.yaml', help='(optional) dataset.yaml path')

    # parser.add_argument('--data', type=str, default= 'models/yolov5s.yaml', help='(optional) dataset.yaml path')
    parser.add_argument('--imgsz', '--img', '--img-size', nargs='+', type=int, default=[240], help='inference size h,w')
    parser.add_argument('--conf-thres', type=float, default=0.25, help='confidence threshold')
    parser.add_argument('--iou-thres', type=float, default=0.45, help='NMS IoU threshold')
    parser.add_argument('--max-det', type=int, default=1000, help='maximum detections per image')
    parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--project', default='run/detect', help='save results to project/name')
    parser.add_argument('--name', default='exp', help='save results to project/name')
    parser.add_argument('--exist-ok', default=True, action='store_true', help='existing project/name ok, do not increment')
    parser.add_argument('--vid-stride', type=int, default=1, help='video frame-rate stride')

    opt = parser.parse_args()
    opt.imgsz *= 2 if len(opt.imgsz) == 1 else 1  # expand
    #print_args(vars(opt))
    args = parser.parse_args(args=[])
    print(args)
    return opt

# 启动Flask应用
if __name__ == '__main__':

    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    # app.run(host='192.168.33.178', port=5000)
    app.run(host='127.0.0.1', port=5000)

    

