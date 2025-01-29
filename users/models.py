from django.db import models
from django.contrib.auth.models import AbstractUser
from .choices import *


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=31, blank=True, null=True)

    def __str__(self):
        return super().__str__()


class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="teacher")
    birth = models.DateField()
    gender = models.CharField(max_length=15, choices=GenderChoice.choices)
    subject = models.ForeignKey('lessons.Subject', on_delete=models.PROTECT, related_name='teachers')
    experience = models.FileField(upload_to="files/%Y/m/%d", blank=True, null=True)

    def __str__(self):
        return f"Teacher(pk = {self.pk})"
