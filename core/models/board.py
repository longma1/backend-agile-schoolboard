from django.db import models

from core.models import StudentProfile, Course


class Board(models.Model):
    board_id = models.UUIDField(primary_key=True)
    owner = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    board_name = models.TextField()
    board_class = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    public = models.BooleanField(default=False)
