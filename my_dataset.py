# import numpy as np
# from torch.utils.data import Dataset
# import os
# import torch
# import json
# from PIL import Image
# from lxml import etree
# root = './datasets/NEU-DET/'
# img_root = os.path.join(root, "JPEGImages")
# labels_root = os.path.join(root, "labels")
# train_txt_path = os.path.join(root, "ImageSets", "Main", "train.txt")
# val_txt_path = os.path.join(root, "ImageSets", "Main", "val.txt")
#
# txt_list = []
#
# with open(train_txt_path) as read:
#     jpg_list = [os.path.join(labels_root, line.strip() + ".txt")
#         for line in read.readlines() if len(line.strip()) > 0]
#
# class VOCDataSet(Dataset):
#     """读取解析PASCAL VOC2007/2012数据集"""
#
#
#         self.
#         # check file
#         for txt_path in txt_list:
#             if os.path.exists(txt_path) is False:
#                 print(f"Warning: not found '{txt_path}', skip this annotation file.")
#                 continue
#
#             self.txt_list.append(txt_path)
#
#     def __len__(self):
#         return len(self.xml_list)
# -*- coding: UTF-8 -*-
# !/usr/bin/env python

# import sys    #导入sys模块
# import re     #导入re模块
# from PIL import Image  #PIL是python的第三方图像处理库
# import shutil
# # sys.path.append('./datasets/NEU-DET/train')   #对于模块和自己写的脚本不在同一个目录下，在脚本开头加sys.path.append(‘引用模块的地址’)：
# import numpy as np
# data = []
# for line in open("./datasets/NEU-DET/ImageSets/Main/train.txt", "r"):  # 设置文件对象并读取每一行文件
#     data.append(line)
# for a in data:
#     # im = Image.open()  # 打开改路径下的line3记录的的文件名
#     # im.save()  # 把文件夹中指定的文件名称的图片另存到该路径下
#     # im.close()
#     path_copy = './datasets/NEU-DET/labels/{}.txt'.format(a[:-1])
#     paste_dir = './datasets/NEU-DET/train/{}.txt'.format(a[:-1])
#     shutil.copy(path_copy, paste_dir)

#!/bin/bash
# Download common models


