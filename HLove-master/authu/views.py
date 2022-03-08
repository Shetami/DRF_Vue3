from django.shortcuts import render
from rest_framework import viewsets, parsers, generics, mixins
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from .castom_permission import IsOwnerProfileOrReadOnly
from .models import AuthUser
from .serializers import UserAuthSerializer


class UserViewCreate(ListCreateAPIView, mixins.UpdateModelMixin):
    queryset = AuthUser.objects.all()
    serializer_class = UserAuthSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset=AuthUser.objects.all()
    serializer_class=UserAuthSerializer
    permission_classes=[IsOwnerProfileOrReadOnly,IsAuthenticated]


