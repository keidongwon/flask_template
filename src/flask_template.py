import sys
import logging
from flask import Flask
from flask_restful import Api
from common.constant import FilePrefix, SystemString
from common import preload, config, errorcode
import routes


app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config['SQLALCHEMY_POOL_RECYCLE'] = 3600
app.config.update(TEMPLATES_AUTO_RELOAD=True)
api = Api(app)
routes.init(api)


def setup():
    try:
        preload.init()
        errorcode.load(FilePrefix.ERRORCODE, config.get("error", "path"))
    except IOError as e:
        print(e)
        sys.exit()


setup()
logging.getLogger().info("%s %s (%s)", SystemString.PROJECT_NAME,
                         SystemString.PROJECT_VERSION,
                         SystemString.PROJECT_UPDATE)

if __name__ == '__main__':
    mode = False
    thread = False
    if config.get("system", "mode") == "debug":
        mode = True
    if config.get("system", "threaded") == "yes":
        thread = True
    app.run(
        debug=mode,
        threaded=thread,
        host=config.get("system", "ip"),
        port=config.get("system", "port")
    )
    logging.getLogger().info("%s finished", SystemString.PROJECT_NAME)
