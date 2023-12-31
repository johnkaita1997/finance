from django.http import HttpResponse
from rest_framework import serializers

from academic_year.serializers import AcademicYearSerializer
from classes.serializers import ClassesSerializer
from school.models import School
from school.serializer import SchoolSerializer
from streams.serializers import StreamsSerializer
from students.models import Student


class StudentSerializer(serializers.ModelSerializer):
    current_Stream_details = StreamsSerializer(source='current_Stream', required=False, read_only=True)
    current_Class_details = ClassesSerializer(source='current_Class', required=False, read_only=True)
    current_Year_details = AcademicYearSerializer(source='current_Year', required=False, read_only=True)
    school_details = serializers.SerializerMethodField(read_only=True)

    def get_school_details(self, obj):
        school_id = obj.school_id
        try:
            school = School.objects.get(id=school_id)
            return SchoolSerializer(school).data
        except School.DoesNotExist as exception:
            return {'error': f"School not found for id {school_id}"}
        except Exception as exception:
            return {'error': f"Bad Request {exception}"}

    class Meta:
        model = Student
        fields = '__all__'
