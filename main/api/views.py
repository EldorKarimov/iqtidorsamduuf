from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from main.models import *
from .serializers import *
from django.utils.translation import gettext_lazy as _
from rest_framework.permissions import IsAuthenticated


class CarouselListAPIView(APIView):
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
    def get(self, request):
        startUpProjects = StartUpProjects.objects.filter(is_available = True).order_by('-created')
        serializer = StartUpProjectSerializer(startUpProjects, many = True)
        data = {
            'success': True,
            'data': serializer.data
        }
        return Response(
            data=data,
            status=status.HTTP_200_OK
        )

class TalentedStudentsListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, talent_type = None):
        if talent_type is not None:
            talents = TalentedStudents.objects.filter(is_available = True, talent_type=talent_type).order_by('-created')
        else:   
            talents = TalentedStudents.objects.filter(is_available = True).order_by('-created')
        serializers = TalentedStudentsSerializer(talents, many = True)
        data = {
            'success': True,
            'data': serializers.data
        }
        return Response(
            data=data,
            status=status.HTTP_200_OK
        )
    

class DocumentsListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, doc_type = None):
        if doc_type is not None:
            docs = Documents.objects.filter(doc_type = doc_type).order_by('-created')
        else:
            docs = Documents.objects.all().order_by('-created')
        serializer = DocumentsSerializer(docs, many = True)
        data = {
            'success': True,
            'data': serializer.data
        }
        return Response(
            data=data,
            status=status.HTTP_200_OK
        )

class CompetitionListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        competitions = Competition.objects.all().order_by('-created')
        serializer = CompetitionSerializer(competitions, many = True)
        data = {
            'success':True,
            'data':serializer.data
        }
        return Response(
            data=data,
            status=status.HTTP_200_OK
        )