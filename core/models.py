from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class StudentProfile(models.Model):
    student_profile_id = models.UUIDField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


# currently the same, adds more field later
class TeacherProfile(models.Model):
    teacher_profile_id = models.UUIDField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created=False, **kwargs):
    if created:
        if instance.is_student:
            StudentProfile.objects.create(student_profile_id=uuid.uuid4(), user=instance)
        if instance.is_teacher:
            TeacherProfile.objects.create(teacher_profile_id=uuid.uuid4(), user=instance)


class Course(models.Model):
    course_id = models.UUIDField(primary_key=True)
    course_name = models.TextField()


class Board(models.Model):
    board_id = models.UUIDField(primary_key=True)
    owner = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    board_name = models.TextField()
    board_class = models.ForeignKey(Course, on_delete=models.CASCADE)
    public = models.BooleanField(default=False)


class Ticket(models.Model):
    TODO = 'TD'
    PROGRESS = 'IP'
    DONE = 'DN'
    SUBMITTED = 'SB'
    RETURNED = 'RT'
    TICKET_STATE_CHOICES = (
        (TODO, 'To Do'),
        (PROGRESS, 'In Progress'),
        (DONE, 'Done'),
        (SUBMITTED, 'Submitted'),
        (RETURNED, 'Returned')
    )
    ticket_id = models.UUIDField(primary_key=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(
        max_length=2,
        choices=TICKET_STATE_CHOICES,
        default=TODO,
    )
