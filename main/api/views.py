from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from main.models import *
from .serializers import *
from django.utils.translation import gettext_lazy as _
from rest_framework.permissions import IsAuthenticated
from shared.utils import get_lang_code
from shared.pagination import CustomPageNumberPagination


class CarouselListAPIView(APIView):
    def get(self, request):
        carousels = Carousel.objects.all().order_by('-created')
        serializer = CarouselSerializer(carousels, many = True)
        data = {
            'success': True,
            'data': serializer.data
        }
        return Response(
            data=data,
            status=status.HTTP_200_OK
        )

class StartUpProjectsListApiView(APIView):
    def get(self, request):
        startUpProjects = StartUpProjects.objects.filter(is_available = True).order_by('-created')
        paginator = CustomPageNumberPagination()
        page_obj = paginator.paginate_queryset(startUpProjects, request)
        serializer = StartUpProjectSerializer(page_obj, many = True, context = get_lang_code(request))
        return Response(
            paginator.get_paginated_response(serializer.data),
            status=status.HTTP_200_OK
        )

class TalentedStudentsListAPIView(APIView):
    def get(self, request, talent_type = None):
        if talent_type is not None:
            talents = TalentedStudents.objects.filter(is_available = True, talent_type=talent_type).order_by('-created')
        else:   
            talents = TalentedStudents.objects.filter(is_available = True).order_by('-created')
        paginator = CustomPageNumberPagination()
        page_obj = paginator.paginate_queryset(talents, request)
        serializer = TalentedStudentsSerializer(page_obj, many = True, context = get_lang_code(request))
        return Response(
            paginator.get_paginated_response(serializer.data),
            status=status.HTTP_200_OK
        )
    

class DocumentsListAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, doc_type = None):
        if doc_type is not None:
            docs = Documents.objects.filter(doc_type = doc_type).order_by('-created')
        else:
            docs = Documents.objects.all().order_by('-created')
        paginator = CustomPageNumberPagination()
        paginator.page_size = 9
        page_obj = paginator.paginate_queryset(docs, request)
        serializer = DocumentsSerializer(page_obj, many = True, context = get_lang_code(request))
        return Response(
            paginator.get_paginated_response(serializer.data),
            status=status.HTTP_200_OK
        )

class CompetitionListAPIView(APIView):
    def get(self, request):
        competitions = Competition.objects.all().order_by('-created')
        paginator = CustomPageNumberPagination()
        page_obj = paginator.paginate_queryset(competitions, request)
        serializer = CompetitionSerializer(page_obj, many = True, context = get_lang_code(request))
        data = {
            'success':True,
            'data':serializer.data
        }
        return Response(
            data=data,
            status=status.HTTP_200_OK
        )