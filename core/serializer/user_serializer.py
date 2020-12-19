from rest_framework import serializers
from core.models import User


class UserSerializer(serializers.ModelSerializer):
    # Taken from https://stackoverflow.com/questions/16857450/how-to-register-users-in-django-rest-framework
    # No clue if its best practice but fk it
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'is_student', 'is_teacher')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_student=validated_data['is_student'],
            is_teacher=validated_data['is_teacher']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
