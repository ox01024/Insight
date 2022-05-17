#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 21:57
# @Author  : waffle
# @Email   : ox01024@163.com
# @File    : translateUtil.py

# 本文文件 所有代码照抄自https://x.hacking8.com/post-414.html
import base64
import hashlib
import json
import string
import random
import requests



def rot13(params):
    t = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    o = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    s = []
    for i in list(params):
        index = o.find(i)
        if index > -1:
            s.append(t[index])
        else:
            s.append(i)
    return ''.join(s)


def caiyun_decode(s):
    s = rot13(s)
    s2 = base64.b64decode(s).decode('utf-8')
    return s2


def generate_jwt():
    url = "https://api.interpreter.caiyunai.com/v1/user/jwt/generate"
    headers = {
        "X-Authorization": "token:qgemv4jr1y38jyq6vhvi",
        "Content-Type": "application/json;charset=UTF-8",
        "app-name": "xy"
    }
    encrypt = hashlib.md5()
    encrypt.update(''.join(random.sample(string.ascii_letters + string.digits, 8)).encode())
    # encrypt.update(get_random_string(10, "qweasdzxcrtyfghvbnuiopjklm1234567890").encode())
    result = encrypt.hexdigest()
    data = {"browser_id": result}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.json()["jwt"], result


def translater(s, jwt, brower_id):
    url = "https://api.interpreter.caiyunai.com/v1/translator"
    headers = {
        "X-Authorization": "token:qgemv4jr1y38jyq6vhvi",
        "Content-Type": "application/json;charset=UTF-8",
        "app-name": "xy",
        "T-Authorization": jwt,
    }
    data = {"source": s.splitlines(), "trans_type": "en2zh", "request_id": "web_fanyi", "media": "text",
            "os_type": "web",
            "dict": False, "cached": True, "replaced": True, "browser_id": brower_id}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.json()


def en2zh(en:str):
    s, s1 = generate_jwt()
    s = translater(en, s, s1)
    return caiyun_decode(s["target"][0])





if __name__ == '__main__':
    print(en2zh('The new Windows Terminal and the original Windows console host, all in the same place!'))
