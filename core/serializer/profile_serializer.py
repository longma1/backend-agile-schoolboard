from rest_framework import serializers
from core.models import StudentProfile


# TODO: idk what to do with this
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
