#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 13:42
# @Author  : waffle
# @Email   : ox01024@163.com
# @File    : githubSearch.py
from loguru import logger
import requests


class gitHub:
    def __init__(self, token: str):
        self.api = "https://api.github.com"
        self.token = token
        self.header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
                       "Accept": "application/vnd.github.v3+json",
                       "Authorization": f"token {self.token}"}

    def repositoriesSearch(self, query: str, per_page: int = 30, page: int = 1):
        try:
            r = requests.get(
                url= f'{self.api}/search/repositories?q={query}&per_page={per_page}&page={page}',
                headers=self.header
            )
            return r.json()
        except Exception as e:
            logger.error(f"[GithubSearch] Search {query} Erro {e}")



def repositorySearch(token,kw):
    Github=gitHub(token)
    return Github.repositoriesSearch(kw)





