#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 16:17
# @Author  : waffle
# @Email   : ox01024@163.com
# @File    : twitter.py
import json,re
from loguru import logger
import requests
from .utils.timeUtil import utc2local



def getCVEnew():
    '''获取CVEnew最新推文并返回结构化数据'''
    try:
        # url="https://cdn.syndication.twimg.com/timeline/profile?callback=__twttr.callbacks.tl_i0_profile_CVEnew_old&dnt=true&domain=cve.mitre.org&lang=en&screen_name=CVEnew&suppress_response_codes=true&t=1832285&tz=GMT+0800&with_replies=false"
        url='https://cdn.syndication.twimg.com/timeline/profile?callback=__twttr.callbacks.tl_i0_profile_CVEnew_old&dnt=true&domain=cve.mitre.org&' \
            'lang=en&screen_name=CVEnew&suppress_response_codes=true&t=1832603&tz=GMT%2B0800&with_replies=false'
        r=requests.get(url=url)
    except Exception as e:
        logger.error(f'[getCVEnew] 获取CVEnew 推文失败 {e}')
        return
    try:
        r_json=json.loads(r.text[47:-2])
        r_html=r_json['body']
        timerex=r'datetime="(.*)"'
        datarex=r'<p class="timeline-Tweet-text" lang="en" dir="ltr">(.*?) <a href="https://t.co/.*" rel="nofollow noopener" dir="ltr" data-expanded-url="https://cve.mitre.org/cgi-bin/cvename.cgi\?name=(.*?)"'
        timelist=re.findall(timerex,r_html)
        softerlist=re.findall(datarex,r_html)
        cveorg='https://cve.mitre.org/cgi-bin/cvename.cgi?name='
        rlist=[{'datetime':utc2local(time),'cveid':text[1],'text':text[0],'url':f'{cveorg}{text[1]}'} for time,text in zip(timelist,softerlist)]
        return rlist
    except Exception as e:
        logger.error(f'[getCVEnew] 结构化CVEnew 推文失败 {e}')
        raise SystemExit