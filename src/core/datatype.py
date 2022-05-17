#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/5 11:34
# @Author  : waffle
# @Email   : ox01024@163.com
# @File    : datatype.py
from collections import OrderedDict
import sqlite3


class AttribDict(OrderedDict):
    """
    AttrDict extends OrderedDict to provide attribute-style access.
    Items starting with __ or _OrderedDict__ can't be accessed as attributes.
    """
    __exclude_keys__ = set()

    def __getattr__(self, name):
        if (name.startswith('__')
                or name.startswith('_OrderedDict__')
                or name in self.__exclude_keys__):
            return super(AttribDict, self).__getattribute__(name)
        else:
            try:
                return self[name]
            except KeyError:
                raise AttributeError(name)

    def __setattr__(self, name, value):
        if (name.startswith('__')
                or name.startswith('_OrderedDict__')
                or name in self.__exclude_keys__):
            return super(AttribDict, self).__setattr__(name, value)
        self[name] = value

    def __delattr__(self, name):
        if (name.startswith('__')
                or name.startswith('_OrderedDict__')
                or name in self.__exclude_keys__):
            return super(AttribDict, self).__delattr__(name)
        del self[name]

class db:
    def __init__(self):
        self.cur=None
    def loaddb(self,path):
        con = sqlite3.connect(path,check_same_thread=False)
        self.cur=con.cursor()