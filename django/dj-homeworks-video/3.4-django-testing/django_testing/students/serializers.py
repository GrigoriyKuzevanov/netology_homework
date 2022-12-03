from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.conf import settings

from students.models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate(self, data):
        if 'students' in data.keys() and len(data['students']) > settings.MAX_STUDENTS_PER_COURSE:
            raise ValidationError('Слишком много студентов на курсе!')
        return data
