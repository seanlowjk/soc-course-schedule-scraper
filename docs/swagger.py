from flasgger import Swagger

SWAGGER_CONFIG = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'api_docs',
            "route": '/api_docs.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/"
}


def init_swagger(app):
    return Swagger(app, config=SWAGGER_CONFIG)
