# api/serializers.py
from rest_framework import serializers
from lessons.models import Lesson
from lessons.models import Class, Subject, Level, Equipment
from users.models import Teacher

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['id', 'title']

class ClassSerializer(serializers.ModelSerializer):
    equipments = EquipmentSerializer(many=True)  # Nested Equipment data

    class Meta:
        model = Class
        fields = ['id', 'title', 'image', 'equipments']

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['id', 'title', 'code']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'email']

class LessonSerializer(serializers.ModelSerializer):
    auditory = ClassSerializer()  # Nested Class data
    teacher = TeacherSerializer()  # Nested Teacher data
    subject = SubjectSerializer()  # Nested Subject data
    level = LevelSerializer()  # Nested Level data

    class Meta:
        model = Lesson
        fields = ['id', 'auditory', 'teacher', 'subject', 'level', 'date', 'time', 'comment']
