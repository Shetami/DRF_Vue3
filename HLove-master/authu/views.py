from django.shortcuts import render
from rest_framework import viewsets, parsers, generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from .castom_permission import IsOwnerProfileOrReadOnly
from .models import AuthUser
from .serializers import UserAuthSerializer


class UserViewCreate(ListCreateAPIView):
    queryset = AuthUser.objects.all()
    serializer_class = UserAuthSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)


class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset=AuthUser.objects.all()
    serializer_class=UserAuthSerializer
    permission_classes=[IsOwnerProfileOrReadOnly,IsAuthenticated]


