from flask import Flask
from flask_restful import Api
from common.constant import FilePrefix
from common.constant import SystemString
from common import preload
from common import config
from common import errorcode
from common import version
import logging
from routes import main


app = Flask(__name__)
app.jinja_env.auto_reload = True
api = Api(app)
api.add_resource(main.Root, '/')


class Service(object):
    def setup(self):
        result_config = config.load(FilePrefix.CONFIG)
        result_errorcode = errorcode.load(FilePrefix.ERRORCODE)
        result_verison = version.load(FilePrefix.VERSION)
        result_preload = preload.init()

        logging.getLogger().info(SystemString.PROJECT_NAME + " " + SystemString.PROJECT_VERSION)
        logging.getLogger().info(result_config)
        logging.getLogger().info(result_errorcode)
        logging.getLogger().info(result_verison)
        logging.getLogger().info(result_preload)

    def finialize(self):
        logging.getLogger().info(SystemString.PROJECT_NAME + " finished")

    def run(self):
        app.run()


if __name__ == '__main__':
    service = Service()
    service.setup()
    service.run()
    service.finialize()
