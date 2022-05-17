#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 14:17
# @Author  : waffle
# @Email   : ox01024@163.com
# @File    : dingding.py

from loguru import logger
import requests
import json


def send(access_token, msg):
    '''
    钉钉Webhook消息推送
    :param access_token: Dingding Token
    :param msg: meeage
    :return:
    '''
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    try:
        r=requests.post(
            url=f"https://oapi.dingtalk.com/robot/send?access_token={access_token}",
            data=json.dumps(msg),
            headers=headers)
        logger.info(f"[钉钉推送] 钉钉Webhook推送成功:{r.text}")
    except Exception as e:
        logger.error(f"[钉钉推送] 钉钉Webhook推送失败:{e}")
