from app_services.student import student_blueprint


def routes(app):
    app.register_blueprint(student_blueprint, url_prefix='/student')
    return app
