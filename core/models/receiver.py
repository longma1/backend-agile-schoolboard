import uuid

from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import StudentProfile, TeacherProfile, User


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created=False, **kwargs):
    if created:
        if instance.is_student:
            StudentProfile.objects.create(student_profile_id=uuid.uuid4(), user=instance)
        if instance.is_teacher:
            TeacherProfile.objects.create(teacher_profile_id=uuid.uuid4(), user=instance)
