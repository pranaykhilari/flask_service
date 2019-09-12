from employee import api_bp


def url(app):
    app.register_blueprint(api_bp, url_prefix='/')
