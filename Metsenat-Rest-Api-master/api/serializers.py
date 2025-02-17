from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import University, Student, Sponsor, StudentSponsor

User = get_user_model()


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'role']


# Login Serializer
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'role', 'avatar']


# University Serializer
class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


# Student Serializer
class StudentSerializer(serializers.ModelSerializer):
    university = UniversitySerializer(read_only=True)

    class Meta:
        model = Student
        fields = '__all__'


# Sponsor Serializer
class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'


# Student-Sponsor Relationship Serializer
class StudentSponsorSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    sponsor = SponsorSerializer(read_only=True)

    class Meta:
        model = StudentSponsor
        fields = '__all__'
