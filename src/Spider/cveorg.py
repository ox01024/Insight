#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 14:33
# @Author  : waffle
# @Email   : ox01024@163.com
# @File    : cveorg.py
from loguru import logger
import requests


def SearchCVE(CVEID:str):
    try:
        r=requests.get(url=f'https://www.cve.org/api/?action=getCveById&cveId={CVEID}',
                       headers={"Accept": "application/json, text/plain, */*",
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
                                "Referer": f"https://www.cve.org/CVERecord?id={CVEID}"})
        return r.json()
    except Exception as e:
        logger.error(f'[Cve_Search] Search {CVEID} Error {e}')



def cverefelist(CVEID:str):
    return SearchCVE(CVEID)['references']['reference_data']


