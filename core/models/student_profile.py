from django.db import models

from core.models import User


class StudentProfile(models.Model):
    student_profile_id = models.UUIDField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
