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
        self.logger = logging.getLogger(__name__)

        #################################################################################################
        # 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        self.logger.addHandler(console)
        log_hander = logging.FileHandler(os.path.join(WORK_SPACE,'logs/devlop.log'))
        log_hander.setLevel(logging.ERROR)
        log_hander.setFormatter(formatter)
        self.logger.addHandler(log_hander)


    def error(self,msg):
        self.logger.error(msg)

    def info(self,msg):
        self.logger.info(msg)

