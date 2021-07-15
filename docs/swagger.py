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
    "specs_route": "/docs/",
}


def init_swagger(app, host, base_path):
    swagger_config = SWAGGER_CONFIG
    swagger_config['swagger_ui_bundle_js'] = '//unpkg.com/swagger-ui-dist@3/swagger-ui-bundle.js'
    swagger_config['swagger_ui_standalone_preset_js'] = '//unpkg.com/swagger-ui-dist@3/swagger-ui-standalone-preset.js'
    swagger_config['jquery_js'] = '//unpkg.com/jquery@2.2.4/dist/jquery.min.js'
    swagger_config['swagger_ui_css'] = '//unpkg.com/swagger-ui-dist@3/swagger-ui.css'
    swagger_config['host'] = host 
    swagger_config['basePath'] = base_path
    return Swagger(app, config=swagger_config)
