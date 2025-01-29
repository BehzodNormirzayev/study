from django.db import models


class UserChoice(models.TextChoices):
    STUDENT = 'STUDENT'
    TEACHER = 'TEACHER'
    ADMIN = 'ADMIN'


class GenderChoice(models.TextChoices):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
