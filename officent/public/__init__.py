# -*- coding: utf-8 -*-
import logging
import os

WORK_SPACE = os.path.dirname(os.path.dirname(__file__))
class Log(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = super(Log, cls).__new__(cls,*args,**kwargs)
        return cls._instance

    def __init__(self):
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename=os.path.join(WORK_SPACE,'logs/devlop.log'),
                            filemode='a')

        #################################################################################################
        # 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)


    def error(self,msg):
        logging.error(msg)

    def info(self,msg):
        logging.info(msg)
