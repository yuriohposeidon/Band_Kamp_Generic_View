from rest_framework import serializers
from .models import Album
from users.serializers import UserSerializer

class AlbumSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only="True")
    class Meta:
        model = Album
        fields = '__all__'  
        extra_kwargs = {"id": {"read_only": True}}