from django.urls import path, include
from avto import views

urlpatterns = [
    path("main/", views.MainPostListAPIView.as_view()),
    path('region/', views.RegionDistrictListApiView.as_view()),
    path('post/region/', views.PostRegionListApiView.as_view()),
    path('post/district/', views.PostDistrictListApiView.as_view()),
    path('post/count/', views.DistrictPostCountListApiView.as_view()),
    path("account/create/", views.AccountCreateApiView.as_view()),
    path("main/<int:pk>/", views.DetailRetrievApiView.as_view())
    ]
