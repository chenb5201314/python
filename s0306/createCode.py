#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/6 22:19
# @Author  : chenb
# @Site    : 
# @File    : createCode.py
# @Software: PyCharm

import qrcode
import io
from PIL import Image, ImageDraw

def get_code_by_str(text):
    if not isinstance(text,str):
        print('请输入字符串参数')
        return None
    qr = qrcode.QRCode(
        version =1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size= 10,
        border= 4,
    )

    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image()
    img_data = io.BytesIO()
    img.save(img_data)
    # print(img_data.getvalue())
    return img_data

if __name__ == '__main__':

    get_code_by_str('http://www.baidu.com/')
