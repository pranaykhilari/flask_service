import requests

url = 'http://127.0.0.1:5000'  # The root url of the flask app


def test_get_all_student():
    # Get all the student
    r = requests.get(url + '/student/get')
    assert r.status_code == 200


def test_negative_get_specific_student():
    # Get Specific student detail
    student_id = 310  # Make sure to replace it with id which is not in database
    r = requests.get(url + '/student/get/{}'.format(student_id))
    assert r.status_code == 200


def test_positive_get_specific_student():
    # Get Specific student detail
    student_id = 31  # Make sure to replace it with id which is in database
    r = requests.get(url + '/student/get/{}'.format(student_id))
    assert r.status_code == 200


