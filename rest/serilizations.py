from rest_framework import serializers
from test_app.models import book
from .models import camera


class camera_s(serializers.ModelSerializer):
    class Meta:
        model = camera
        fields = '__all__'


class book_s(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = '__all__'
