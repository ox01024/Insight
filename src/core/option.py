#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 22:57
# @Author  : waffle
# @Email   : ox01024@163.com
# @File    : option.py
from .data import paths,conf,db
import yaml
from loguru import logger

def setpaths(root_path:str):
    paths.ROOTPATH=root_path

def _setconfig():
    with open(f"{paths.ROOTPATH}/config.yaml", 'r', encoding='utf-8') as ymlfile:
        config = yaml.load_all(ymlfile, Loader=yaml.SafeLoader)
        for data in config:
            conf.GithubToken=data['GithubToken']
            conf.plugins=data['plugins']
def _setdb():
    db.loaddb(f"{paths.ROOTPATH}/insight.db")


def init():
    _setconfig()
    _setdb()











def banner():
    msg='''
 ___           _       _     _
|_ _|_ __  ___(_) __ _| |__ | |_
 | || '_ \/ __| |/ _` | '_ \| __|
 | || | | \__ \ | (_| | | | | |_
|___|_| |_|___/_|\__, |_| |_|\__|
                 |___/
'''
    print(msg)
