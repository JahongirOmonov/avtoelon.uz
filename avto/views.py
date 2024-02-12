from django.shortcuts import render
from rest_framework import routers, serializers, viewsets, generics
from avto.models import Post, Region, District, Account
from avto.serializers import (PostSerializer, 
                              RegionDistrictSerializer, 
                              PostSerializerRegionSerializer,
                              PostSerializerDistrictSerializer,
                              DistrictPostCountSerializer,
                              AccountSerializer,
                              DetailSerializer)
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework import filters

# Create your views here.
class MainPostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all().order_by("-published_at")
    serializer_class = PostSerializer
    filterset_fields = ("subcategory__category",)


class RegionDistrictListApiView(generics.ListAPIView):
    serializer_class = RegionDistrictSerializer
    queryset = Region.objects.prefetch_related('districts').all()


class PostRegionListApiView(generics.ListAPIView):
    serializer_class = PostSerializerRegionSerializer
    queryset = Post.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['district__region__title']

    # def get_queryset(self):
    #     return Post.objects.filter(published=self.request.user).all()

class PostDistrictListApiView(generics.ListAPIView):
    serializer_class = PostSerializerDistrictSerializer
    queryset = Post.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['district__title']


class DistrictPostCountListApiView(generics.ListAPIView):
    serializer_class=DistrictPostCountSerializer
    queryset=District.objects.all()

class AccountCreateApiView(generics.CreateAPIView):
    queryset=Account.objects.all()
    serializer_class=AccountSerializer

class DetailRetrievApiView(generics.RetrieveAPIView):
    queryset=Post.objects.all()
    serializer_class = DetailSerializer









