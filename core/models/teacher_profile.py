from django.db import models
from .user import User


# currently the same as student profile, adds more field later
class TeacherProfile(models.Model):
    teacher_profile_id = models.UUIDField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
