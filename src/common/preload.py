# -*- coding: utf-8 -*-
import logging
import socket
from pybolt.log.rotation_log import create_date_rotating_file_handler
from pybolt.database.alchemy_pool import thealchemy
from pybolt.database.helper import alchemyhelper
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

    connect_string = "%s://%s:%s@%s:%d/%s" % \
        ('mysql',
        config.get("db", "user"),
        config.get("db", "password"),
        config.get("db", "host"),
        config.get("db", "port"),
        config.get("db", "dbname"))
    # db, uid, pwd, host, port, dbname
    thealchemy.create_pool(connect_string, 0)
    alchemyhelper.set_instance(thealchemy)

    return "preload initialized"
