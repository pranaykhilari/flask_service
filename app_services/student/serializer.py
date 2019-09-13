from flask_marshmallow import Marshmallow

from app import app

ma = Marshmallow(app)


class StudentSerializer(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'phone_num')


student_schema = StudentSerializer()
students_schema = StudentSerializer(many=True)
