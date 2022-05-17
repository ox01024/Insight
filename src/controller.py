#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/5 13:41
# @Author  : waffle
# @Email   : ox01024@163.com
# @File    : controller.py
from .core.data import conf,db
from loguru import logger
import sqlite3
from .Spider.twitter import getCVEnew
from .Spider.cveorg import cverefelist
from .Spider.githubSearch import repositorySearch
from .Spider.utils.translateUtil import en2zh
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
from .plugin import send

def createdb():
    tweets='''create table tweets
(
    timestamp text  not null,
    cveid     text not null
);

create unique index tweets_cveid_uindex
    on tweets (cveid);'''
    conn=db.cur
    conn.executescript(tweets)



def oldCVEsve():
    '''历史推送CVE入库 用来求新'''
    oldCVElist=getCVEnew()
    for tweets in oldCVElist:
        inst_sql="INSERT INTO tweets (timestamp, cveid) VALUES ('{}','{}')".format(tweets['datetime'],tweets['cveid'])
        conn = db.cur
        conn.executescript(inst_sql)


def oldCVElist():
    '''获取数据库中已存在的cve list'''
    conn=db.cur
    conn.execute('SELECT cveid FROM tweets')
    return [cveid[0] for cveid in conn.fetchall()]

def seekNew():
    '''监控变更'''
    oldlist=oldCVElist()
    logger.info('newCVE 检查')
    for tweets in getCVEnew():
        if not tweets['cveid'] in oldlist:
            logger.info("监测到新的CVE,{}".format(tweets['cveid']))
            newCVEsend(tweets)
            inst_sql = "INSERT INTO tweets (timestamp, cveid) VALUES ('{}','{}')".format(tweets['datetime'],
                                                                                         tweets['cveid'])
            conn = db.cur
            conn.executescript(inst_sql)


def cverefe(cveid:str):
    '''refsource Messg'''
    msg=''
    for refe in cverefelist(cveid):
        msg+=f'[{refe["name"]}]({refe["url"]}) \n'
    return msg

def repositoryfind(cve:str):
    githutoken=conf["GithubToken"]
    resultJson=repositorySearch(githutoken,cve)
    repositorytext=""
    for r in resultJson["items"]:
        repositorytext+=r["full_name"]+"\n"
        repositorytext+=r["html_url"]+"\n"
    return repositorytext




def newCVEsend(tweets):
    '''内容富化'''
    cveid=tweets["cveid"]
    entext=tweets["text"]
    zhtext=en2zh(tweets["text"])
    reference=cverefe(tweets["cveid"])
    time=tweets["datetime"]
    cveorg=tweets["url"]
    repository=repositoryfind(cveid)
    newCVEinfo={
        "cveid": cveid,
        "text": "{}\t\n{}".format(entext,zhtext),
        "time":time,
        "cveorg": cveorg,
        "Reference":reference,
        "repository":repository
    }
    send(newCVEinfo)




def start():
    # 检查是否存在历史数据
    try:
        createdb()
        oldCVEsve()
        scheduler = BlockingScheduler()
        intervalTrigger = IntervalTrigger(minutes=5)
        scheduler.add_job(seekNew,intervalTrigger,id='myjob')
        scheduler.start()
    except sqlite3.OperationalError:
        # 开始监控
        scheduler = BlockingScheduler()
        intervalTrigger = IntervalTrigger(minutes=5)
        scheduler.add_job(seekNew,intervalTrigger,id='myjob')
        scheduler.start()





