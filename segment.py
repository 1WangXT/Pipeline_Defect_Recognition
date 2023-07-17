import os
import time
import json

import torch
from torchvision import transforms
import numpy as np
from PIL import Image

from src import lraspp_mobilenetv3_large


def time_synchronized():
    torch.cuda.synchronize() if torch.cuda.is_available() else None
    return time.time()


def main():
    classes = 3
    weights_path = "./save_weights/model_746.pth"
    save_path = "./runs/segment/"
    img_paths = "./dataset/VOCdevkit/VOC2012/JPEGImages/"
    palette_path = "./palette.json"
    assert os.path.exists(weights_path), f"weights {weights_path} not found."
    assert os.path.exists(img_paths), f"image {img_paths} not found."
    assert os.path.exists(palette_path), f"palette {palette_path} not found."
    with open(palette_path, "rb") as f:
        pallette_dict = json.load(f)
        pallette = []
        for v in pallette_dict.values():
            pallette += v

    # get devices
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print("using {} device.".format(device))

    # create model
    model = lraspp_mobilenetv3_large(num_classes=classes+1)

    # load weights
    weights_dict = torch.load(weights_path, map_location='cpu')['model']
    model.load_state_dict(weights_dict)
    model.to(device)
    data_transform = transforms.Compose([transforms.Resize(240),
                                         transforms.ToTensor(),
                                         transforms.Normalize(mean=(0.485, 0.456, 0.406),
                                                              std=(0.229, 0.224, 0.225))])
    # load image
    for img_path in os.listdir(img_paths):
        # 判断是否为图片文件
        if img_path.endswith('.jpg') or img_path.endswith('.png') or img_path.endswith('.JPG'):
            # 使用PIL库打开图片文件
            img_path1 = os.path.join(img_paths, img_path)

            original_img = Image.open(img_path1)

            img = data_transform(original_img)
            # expand batch dimension
            img = torch.unsqueeze(img, dim=0)

            model.eval()  # 进入验证模式
            with torch.no_grad():
                # init model
                img_height, img_width = img.shape[-2:]
                init_img = torch.zeros((1, 3, img_height, img_width), device=device)
                model(init_img)

                t_start = time_synchronized()
                output = model(img.to(device))
                t_end = time_synchronized()
                print("inference time: {}".format(t_end - t_start))

                prediction = output['out'].argmax(1).squeeze(0)
                prediction = prediction.to("cpu").numpy().astype(np.uint8)
                mask = Image.fromarray(prediction)
                mask.putpalette(pallette)
                # print(save_path+img_path[:-3]+'png')
                mask.save(save_path+img_path[:-3]+'png')


if __name__ == '__main__':
    main()
