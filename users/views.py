from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserRegistrationSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class UserRegister(ModelViewSet):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all().order_by("-id")



class UserCount(APIView):
    queryset = User.objects.all().count()

    def get(self, request):
        return Response(self.queryset)