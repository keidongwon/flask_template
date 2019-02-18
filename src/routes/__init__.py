from routes import main


def init(api):
    api.add_resource(main.Root, '/')
    api.add_resource(main.Version, '/version')
