from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from django.utils.translation import gettext_lazy as _
from courses.models import Author, Course
from .serializers import AuthorSerializer, CourseSerializer
from shared.utils import get_lang_code
from shared.pagination import CustomPageNumberPagination
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class CourseListAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'course_type',
                openapi.IN_QUERY,
                description="The type of the course",
                type=openapi.TYPE_STRING,
                required=True,
                enum=[choice[0] for choice in Course.COURSE_TYPE],  # to provide possible choices
            )
        ]
    )
    def get(self, request, course_type):
        courses = Course.objects.filter(course_type = course_type).order_by('-created')
        paginator = CustomPageNumberPagination()
        page_obj = paginator.paginate_queryset(courses, request)
        serializer = CourseSerializer(page_obj, many = True, context = get_lang_code(request))
        return Response(
            paginator.get_paginated_response(serializer.data),
            status=status.HTTP_200_OK
        )