import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_course(client, course_factory):
    course = course_factory()
    # response = client.get(f'/api/v1/courses/{course.id}/')
    response = client.get('/api/v1/courses/', data={'id': course.id})
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == course.name


@pytest.mark.django_db
def test_get_courses(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    data = response.json()
    for i, c in enumerate(data):
        assert c['name'] == courses[i].name


@pytest.mark.django_db
def test_filter_id(client, course_factory):
    courses = course_factory(_quantity=10)
    examp_course = courses[2]
    response = client.get(f'/api/v1/courses/?id={examp_course.id}')
    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == examp_course.id
    filter_course = Course.objects.filter(id=examp_course.id)
    assert filter_course[0].id == examp_course.id


@pytest.mark.django_db
def test_filter_name(client, course_factory):
    courses = course_factory(_quantity=10)
    examp_course = courses[2]
    response = client.get(f'/api/v1/courses/?name={examp_course.name}')
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == examp_course.name
    filter_course = Course.objects.filter(name=examp_course.name)
    assert filter_course[0].name == examp_course.name


@pytest.mark.django_db
def test_create_course(client):
    count = Course.objects.count()
    response = client.post('/api/v1/courses/', data={'name': 'test_name'})
    assert response.status_code == 201
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_update_course(client, course_factory):
    course = course_factory()
    response = client.patch(f'/api/v1/courses/{course.id}/', data={'name': 'test_name'})
    assert response.status_code == 200
    filter_courses = Course.objects.filter(id=course.id)
    assert filter_courses[0].name == 'test_name'


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course = course_factory()
    count = Course.objects.count()
    response = client.delete(f'/api/v1/courses/{course.id}/')
    assert response.status_code == 204
    assert Course.objects.count() == count - 1


@pytest.mark.django_db
@pytest.mark.parametrize('val, status_code, test_name', [(1, 201, 'a'), (0, 400, 'b')])
def test_students_in_course_validation(val, status_code, test_name, settings, client, student_factory):
    settings.MAX_STUDENTS_PER_COURSE = val
    student = student_factory()
    response = client.post('/api/v1/courses/', data={'name': test_name, 'students': [student.id]})
    assert response.status_code == status_code
