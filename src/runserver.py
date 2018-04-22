import sys
import logging
from flask import Flask
from flask_restful import Api
from common.constant import FilePrefix, SystemString
from common import preload, config, errorcode, version
import routes


app = Flask(__name__)
app.jinja_env.auto_reload = True
api = Api(app)
routes.init(api)


def setup():
    try:
        config.load(FilePrefix.CONFIG)
        preload.init()
        errorcode.load(FilePrefix.ERRORCODE)
        version.load(FilePrefix.VERSION)
    except IOError as e:
        print(e)
        sys.exit()


def run():
    app.config.update(TEMPLATES_AUTO_RELOAD=True)
    app.run(
        host='0.0.0.0',
        port=5000
    )


if __name__ == '__main__':
    setup()
    logging.getLogger().info("%s %s", SystemString.PROJECT_NAME, SystemString.PROJECT_VERSION)
    run()
    logging.getLogger().info("%s finished", SystemString.PROJECT_NAME)
