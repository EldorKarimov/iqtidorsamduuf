from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from django.utils.translation import gettext_lazy as _
from courses.models import Author, Course
from .serializers import AuthorSerializer, CourseSerializer

class CourseListAPIView(APIView):
    def get(self, request, course_type):
        courses = Course.objects.filter(course_type = course_type).order_by('-created')
        serializer = CourseSerializer(courses, many = True)
        data = {
            'success': True,
            'data': serializer.data
        }
        return Response(
            data=data,
            status=status.HTTP_200_OK
        )