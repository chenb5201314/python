# !/user/bin/env python
# -*- coding:utf-8 -*-
import requests


#    分析网页结构
#   请求的url 网址
# 请求的方式 get /post
#    请求的参数



'''
    校验验证码
    Request URL:https://kyfw.12306.cn/passport/captcha/captcha-check
    Request Method:POST
    请求参数：
    answer:113,51,46,118,208,112,272,119
    login_site:E
    rand:sjrand
'''


def login():
        #拿到验证码
        request = requests.session()

        response = request.get('https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.24598181280398213')
        code_img = response.content
        with open('code_img.png','wb') as fn:
            fn.write(code_img)

        code = input('请输入验证码坐标：')

        data  = {'answer':code,
                 'login_site':'E',
                 'rand':'sjrand'}
        request.post('https://kyfw.12306.cn/passport/captcha/captcha-check',data=data)
        print(response.text)
        data = {
            'username':'uesr.name',
            'password':'user.password',
            'appid':'otn'
        }
        url = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
        response = request.post(url)

    
login()
