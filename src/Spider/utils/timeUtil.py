#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 21:26
# @Author  : waffle
# @Email   : ox01024@163.com
# @File    : timeUtil.py
from datetime import datetime

def utc2local( utc_dtm ):
    utc_dtm = datetime.strptime(utc_dtm, '%Y-%m-%dT%H:%M:%S+0000')
    # UTC 时间转本地时间（ +8:00 ）
    local_tm = datetime.fromtimestamp( 0 )
    utc_tm = datetime.utcfromtimestamp( 0 )
    offset = local_tm - utc_tm
    return utc_dtm + offset



