import argparse

from flask import Flask, request, jsonify, render_template, send_file, flash
import torch
import os
# from detect import  run,main
from train import run,main,parse_opt
from flask_cors import *
import json
app = Flask(__name__)


# 定义路由
@app.route('/train', methods=['GET', 'POST'])
def upload():
    CORS(app, supports_credentials=True)
    if request.method == 'POST':  #post是一种请求方式
        opt = parse_opt()
        main(opt)

    return render_template('index.html')

# @app.route('/sh', methods=['GET', 'POST'])  #定义新路由，显示图片
# def hello_world():


# 启动Flask应用
if __name__ == '__main__':

    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(host='192.168.1.22', port=5000)

    

