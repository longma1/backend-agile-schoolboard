from django.db import models


class Course(models.Model):
    course_id = models.UUIDField(primary_key=True)
    course_name = models.TextField()
