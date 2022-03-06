from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("", views.MangaList.as_view(), name='list'),
    path("detail/<slug:slug>/", views.MangaDetailView.as_view(), name='manga_detail'),
    path("read/<slug:manga_slug>/", views.MangaSliderView.as_view(), name='manga_slider'),
]
