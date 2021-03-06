from json import dumps, loads

from flask import Flask, request, make_response
from flask_cors import CORS, cross_origin
from flasgger import swag_from
from redis import Redis
from docs.swagger import init_swagger
from docs.get_module import SPECS_DICT
from utils.constants import CACHE_TIMEOUT, DB, HOST, PORT, SWAGGER_HOST, SWAGGER_PATH
from utils.script import get_module_data

from main.config import CONFIG

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'
swagger = init_swagger(app, CONFIG[SWAGGER_HOST], CONFIG[SWAGGER_PATH])
cache = Redis(host=CONFIG[HOST], port=CONFIG[PORT], db=CONFIG[DB])


@app.route('/api', methods=["GET"])
@cross_origin()
@swag_from(SPECS_DICT)
def get_module():
    """Endpoint for returning module information from SoC Course Website. 
    """
    module_code = request.args.get("module")
    if module_code is None:
        return make_response(dumps({
            "message": "Module not found"
        }), 404)

    cache_result = cache.get(module_code)
    if cache_result is not None:
        return loads(cache_result)

    result = get_module_data(module_code.upper())

    if result is None:
        return make_response(dumps({
            "message": "Module not found"
        }), 404)

    cache.set(name=module_code, value=dumps(result), ex=CACHE_TIMEOUT)
    return make_response(result, 200)
