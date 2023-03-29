from rest_framework.serializers import ModelSerializer
from .models import User

class UserRegistrationSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "email", "username"]
