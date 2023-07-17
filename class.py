import os
import json

import torch
from PIL import Image
from torchvision import transforms
import matplotlib.pyplot as plt

from model import GoogLeNet

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

def main(img_paths):
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    data_transform = transforms.Compose(
        [transforms.Resize((320, 240)),
         transforms.ToTensor(),
         transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
    # read class_indict
    json_path = './class_indices.json'
    assert os.path.exists(json_path), "file: '{}' dose not exist.".format(json_path)
    with open(json_path, "r") as f:
        class_indict = json.load(f)

    # create model
    import torchvision
    model = torchvision.models.googlenet(num_classes=3)
    # model = GoogLeNet(num_classes=3, aux_logits=False).to(device)
    # load image

    # load model weights
    weights_path = "./best.pth"
    assert os.path.exists(weights_path), "file: '{}' dose not exist.".format(weights_path)
    missing_keys, unexpected_keys = model.load_state_dict(torch.load(weights_path, map_location=device), strict=False)

    result = {}
    for source in os.listdir(img_paths):
        # 判断是否为图片文件
        if source.endswith('.jpg') or source.endswith('.png') or source.endswith('.JPG'):
            # 使用PIL库打开图片文件
            img_path = os.path.join(img_paths, source)

            assert os.path.exists(img_path), "file: '{}' dose not exist.".format(img_path)
            img = Image.open(img_path)
            # plt.imshow(img)
            # [N, C, H, W]
            img = data_transform(img)
            # expand batch dimension
            img = torch.unsqueeze(img, dim=0)

            model.eval()
            with torch.no_grad():
                # predict class
                output = torch.squeeze(model(img.to(device))).cpu()
                predict = torch.softmax(output, dim=0)
                predict_cla = torch.argmax(predict).numpy()

            print_res = "class: {}   prob: {:.3}".format(class_indict[str(predict_cla)],
                                                         predict[predict_cla].numpy())
            result[return_img_stream(img_path)] = print_res
    for i in result.values():
        print(i)

    return result
if __name__ == '__main__':
    img_paths = "./edu_data/train/bubbling/"
    main(img_paths)
