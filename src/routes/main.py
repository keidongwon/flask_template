from flask_restful import Resource
from flask import session, request, render_template, make_response


class Root(Resource):
    def get(self):
        uid = request.cookies.get("uid")
        headers = {'Content-Type': 'text/html'}
        data = dict()
        data['uid'] = uid
        if not uid:
            data['url'] = '/login/'
            data['name'] = '로그인'
            data['class'] = 'btn-success'
        else:
            data['url'] = '/logout/'
            data['name'] = '로그아웃'
            data['class'] = 'btn-warning'

        response = make_response(render_template('index.html', messages=data), 200, headers)
        return response
