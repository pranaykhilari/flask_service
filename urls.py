from app_services.student import student_blueprint
from app_services.student_registration import student_registration


def routes(app):
    app.register_blueprint(student_blueprint, url_prefix='/student')
    app.register_blueprint(student_registration, url_prefix='/registration')
    return app
