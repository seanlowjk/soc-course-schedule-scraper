from flask import Flask, request, abort 
from json import dumps 
from utils.script import get_module_data

app = Flask(__name__)

@app.route('/', methods=["GET"])
def get_module():
    module_code = request.args.get("module")
    if module_code is None:
        abort(404)

    result = get_module_data(module_code.upper())

    if result is None: 
        return dumps({
            "message": "Module not found"
        })

    return result
