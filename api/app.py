import os
from functools import wraps

from flask import Flask, Response, abort, request
from flask_pydantic import validate

from .errors import errors
from .meat import do_something
from .schemas import APIRequest

app = Flask(__name__)
app.register_blueprint(errors)


def require_apikey(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        if request.headers.get('X-Api-Key') and request.headers.get('X-Api-Key') == os.environ.get(
            "USER_API_KEY"
        ):
            return view_function(*args, **kwargs)
        else:
            abort(401)

    return decorated_function


@app.route("/")
def index():
    return Response("No Scale Deployable Flask API", status=200)


@app.route("/v1/health")
def show_health():
    return Response("OK", status=200)


@app.route("/v1/test-endpoint", methods=["POST"])
@validate()
@require_apikey
def assemble_map(body: APIRequest):
    data = do_something(dict(body)['data'])

    return Response(data, status=200)
