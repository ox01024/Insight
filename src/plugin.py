#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/7 21:12
# @Author  : waffle
# @Email   : ox01024@163.com
# @File    : plugin.py
from .core.data import conf
from .plugins.dingding import send as dingsend



def send(msg:dict):
    for k,v in conf["plugins"].items():
        if v["enabled"]:
            sendplugin(k,msg)




def sendplugin(plugin:str,msg:dict):
    if plugin=="Dingding":
        dingDingSend(conf["plugins"][plugin]['token'],msg)



def dingDingSend(token:str,msg:dict):
    text=f'## {msg["cveid"]} \n'
    text+=f'> {msg["text"]} \n \n'
    text+=f'#### Reference: \n{msg["Reference"]} \n'
    text += f'#### repository \n {msg["repository"]} \n' if msg["repository"] else ""
    text+=f'##### {(msg["time"])} [查看详情]({msg["cveorg"]}) \n'
    jmsg = {
        "msgtype": "markdown",
        "markdown": {
            "title": msg['cveid'],
            "text": text
        }
    }

    dingsend(token,jmsg)

