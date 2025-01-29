from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


User = get_user_model()



class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Equipment(BaseModel):
    title = models.CharField(max_length=31)
    objects = models.Manager()

    def __str__(self):
        return self.title


class Class(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/%Y/m/%d")
    equipments = models.ManyToManyField(Equipment, related_name="classes")

    objects = models.Manager()

    def __str__(self):
        return self.title


class Level(BaseModel):
    title = models.CharField(max_length=31)
    code = models.CharField(max_length=31, unique=True)

    objects = models.Manager()
    def __str__(self):
        return self.title


class Subject(BaseModel):
    title = models.CharField(max_length=31)
    objects = models.Manager()

    def __str__(self):
        return self.title


class Lesson(BaseModel):

    auditory = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='lessons')
    teacher = models.ForeignKey('users.Teacher', on_delete=models.CASCADE, related_name="lessons")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="lessons")
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name="lessons")

    date = models.DateField()
    time = models.TimeField()

    comment = models.CharField(max_length=511, blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return f"{self.__class__.__name__}(pk = {self.pk})"