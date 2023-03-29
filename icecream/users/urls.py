from rest_framework import routers
from .views import UserRegister, UserCount
from django.urls import path, include
from django.http import HttpRequest

request = HttpRequest()
router = routers.DefaultRouter()
router.register(r'users', UserRegister)


urlpatterns = [
    path('', include(router.urls)),
    path('users/all', UserCount.as_view())
    # path('index.html', UserCount.my_view, name='index.html')
    # path('', .my_view, name='my-view')
]