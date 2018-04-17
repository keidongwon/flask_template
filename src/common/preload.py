# -*- coding: utf-8 -*-
import logging
import socket
from pybolt.log.rotation_log import create_date_rotating_file_handler
from common import config
from common.constant import SystemString


def init():
    """
    프로그램의 시작 (flask run) 전에 초기화 할 작업을 이곳에서 처리합니다.
    """

    log_format = logging.Formatter('%%(asctime)s.%%(msecs)d\t%s\t%s\t%%(levelname)s\t%%(name)s\t %%(message)s'
                                   % (SystemString.PROJECT_LOG, socket.gethostbyname(socket.gethostname())),
                                   datefmt="%Y-%m-%d %H:%M:%S")
    create_date_rotating_file_handler(log_path=config.get("log", "path"),
                                      log_name=config.get("log", "prefix"),
                                      log_format=log_format,
                                      log_level=logging.getLevelName(config.get("log", "level")),
                                      console=config.get("log", "console"))

    return "preload initialized"
