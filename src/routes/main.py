from flask_restful import Resource
from flask import request, render_template, make_response


class Root(Resource):
    def get(self):
        uid = request.cookies.get("uid")
        headers = {'Content-Type': 'text/html'}
        data = dict()
        data['uid'] = uid
        response = make_response(render_template('index.html', messages=data), 200, headers)
        return response
