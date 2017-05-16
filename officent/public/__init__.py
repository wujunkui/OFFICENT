# -*- coding: utf-8 -*-
import logging
import os

import time
from flask import current_app, url_for
from flask_login import current_user
from werkzeug.utils import secure_filename

WORK_SPACE = os.path.dirname(os.path.dirname(__file__))


class Log(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Log, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        self.logger.addHandler(console)
        log_hander = logging.FileHandler(os.path.join(WORK_SPACE, 'logs/devlop.log'))
        log_hander.setLevel(logging.ERROR)
        log_hander.setFormatter(formatter)
        self.logger.addHandler(log_hander)

    def error(self, msg):
        self.logger.error(msg)

    def info(self, msg):
        self.logger.info(msg)


def get_time_str():
    return '{0}'.format(time.time())


def save_upload_file(file_hander, type='avatar'):
    '''
    Save files to stream
    :param file_hander:
    :param type: avatar or audio or img
    :return: url_path or None
    '''
    real_filename = secure_filename(file_hander.filename)
    ext = real_filename.rsplit('.', 1)[1]
    if type == 'avatar':
        allow_file = current_app.config['ALLOW_IMGE']
        save_dirpath = os.path.join(current_app.config['UPLOAD_DIR'], current_user.user_name, 'avatar')
    elif type == 'audio':
        allow_file = current_app.config['ALLOW_AUDIO']
        save_dirpath = os.path.join(current_app.config['UPLOAD_DIR'], current_user.user_name, 'audios')
    elif type == 'img':
        allow_file = current_app.config['ALLOW_IMGE']
        save_dirpath = os.path.join(current_app.config['UPLOAD_DIR'], current_user.user_name, 'imgs')
    else:
        return None
    if not os.path.exists(save_dirpath):
        os.makedirs(save_dirpath)
    if not ext in allow_file:
        return None
    save_filepath = os.path.join(save_dirpath,get_time_str() + '_' + real_filename)
    file_hander.save(save_filepath)
    url_path = save_filepath.replace(current_app.config['STATIC_PATH'],'')
    return url_path
