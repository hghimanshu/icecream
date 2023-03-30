# from rest_framework import routers
from .views import UserRegister, UserData
from django.urls import path, include


# router = routers.DefaultRouter()
# router.register(r'users', UserRegister)


urlpatterns = [
    # path('', include(router.urls)),
    # path('users/all', UserCount.as_view()),
    path('users/', UserRegister.as_view(), name='registration'),
    path('users/collate', UserData.as_view()),
]