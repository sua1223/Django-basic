from django.shortcuts import render
from rest_framework import generics

from .models import Video, DetectResult
from .serializers import VideoSerializer, ResultSerializer

# Create your views here.
class ListVideo(generics.ListCreateAPIView):
    videos = Video.objects.all()
    serializer_class = VideoSerializer


class ListResult(generics.ListCreateAPIView):
    results = DetectResult.objects.all()
    serializer_class = ResultSerializer