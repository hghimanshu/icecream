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

    def get(self, request):
        queryset = User.objects.all().count()
        # render(request, 'E:\\miscellaneous\\singlePageWebsite\\icecream\\users\\templates\\index.html')
        # return Response(queryset)
        return render(request, 'E:\\miscellaneous\\singlePageWebsite\\icecream\\users\\templates\\index.html')
    # def my_view(self, request):
    #     return