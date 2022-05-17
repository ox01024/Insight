#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 13:39
# @Author  : waffle
# @Email   : ox01024@163.com
# @File    : insight.py
from src.core.option import setpaths,init,banner
import os,time
from src.controller import start
from loguru import logger

def module_path():
    """
    This will get us the program's directory
    """
    return os.path.dirname(os.path.realpath(__file__))


def main():
    banner()
    try:
        setpaths(module_path())
        init()
        print(f'[*] starting at {time.strftime("%X")}\n')
    except Exception as e:
        logger.error(f'init Error {e}')
        raise SystemExit
    try:
        start()
    except KeyboardInterrupt:
        raise SystemExit
    finally:
        print(f'\n[*] shutting down at {time.strftime("%X")}\n\n')


if __name__ == '__main__':
    main()

