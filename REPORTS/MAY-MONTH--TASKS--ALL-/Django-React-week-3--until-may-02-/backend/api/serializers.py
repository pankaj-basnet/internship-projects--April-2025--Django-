# ================================
# D:\GROW_CTS\PANKAJ-PROJECTS-\REPORTS\MAY-MONTH--TASKS--ALL-\Django-React-week-3--until-may-02-\backend\api\serializers.py
# ================================

# from django.contrib.auth.models import User
from .models import User
from rest_framework import serializers
from .models import Note


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = [ # this code  after register/login in react # 250429
            "id",
            "uuid",
            "name",
            "bio",
            "email",
        ]

        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}
