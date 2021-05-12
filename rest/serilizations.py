from rest_framework import serializers
from test_app.models import book
from .models import camera, checker


class checker_s(serializers.ModelSerializer):
    class Meta:
        model = checker
        fields = '__all__'


class camera_s(serializers.ModelSerializer):
    class Meta:
        model = camera
        fields = '__all__'


class book_s(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = '__all__'
