from django.urls import path

from authu import views

urlpatterns = [
    path('profile/', views.UserViewCreate.as_view()),
    path('profile/<int:pk>', views.UserProfileDetailView.as_view()),
]