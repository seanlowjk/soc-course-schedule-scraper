from json import dumps, loads

from flask import Flask, abort, request
from redis import Redis
from utils.constants import CACHE_TIMEOUT, DB, HOST, PORT
from utils.script import get_module_data

from main.config import CONFIG

app = Flask(__name__)
cache = Redis(host=CONFIG[HOST], port=CONFIG[PORT], db=CONFIG[DB])


@app.route('/', methods=["GET"])
def get_module():
    module_code = request.args.get("module")
    if module_code is None:
        abort(404)

    cache_result = cache.get(module_code)
    if cache_result is not None:
        return loads(cache_result)

    result = get_module_data(module_code.upper())

    if result is None:
        return dumps({
            "message": "Module not found"
        })

    cache.set(name=module_code, value=dumps(result), ex=CACHE_TIMEOUT)
    return result
