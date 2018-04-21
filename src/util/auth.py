from flask import redirect, request


def check_auth(functor):
    def decorated(*args, **kwargs):
        if request.cookies.get('uid') is None:
            return redirect('/login')
        return functor(*args, **kwargs)
    return decorated
