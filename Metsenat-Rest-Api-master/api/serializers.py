from rest_framework import serializers
from .models import User, Student, Sponsor, StudentSponsor, PaymentSummary
from django.db import models


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['full_name', 'degree', 'contract_price', 'university']


class StudentSponsorSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source="student.full_name", read_only=True)
    degree = serializers.CharField(source="student.degree", read_only=True)
    university = serializers.CharField(source="student.university.name", read_only=True)
    contract_amount = serializers.IntegerField(source="student.contract_price", read_only=True)
    amount_spent = serializers.IntegerField(source="sponsor.amount", read_only=True)

    class Meta:
        model = StudentSponsor
        fields = ['full_name', 'degree', 'university', 'contract_amount', 'amount_spent', 'created_at']


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ['full_name', 'phone', 'progress', 'organization_name', 'sponsor_status']


class AddStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['full_name', 'phone_number', 'degree', 'contract_price', 'university']


class PaymentSummarySerializer(serializers.ModelSerializer):
    total_paid = serializers.SerializerMethodField()
    total_requested = serializers.SerializerMethodField()
    total_needed = serializers.SerializerMethodField()

    class Meta:
        model = PaymentSummary
        fields = ['total_paid', 'total_requested', 'total_needed', 'created_at']

    def get_total_paid(self, obj):
        return Sponsor.objects.aggregate(total_paid=models.Sum('amount'))['total_paid'] or 0

    def get_total_requested(self, obj):
        return Student.objects.aggregate(total_requested=models.Sum('contract_price'))['total_requested'] or 0

    def get_total_needed(self, obj):
        total_requested = self.get_total_requested(obj)
        total_paid = self.get_total_paid(obj)
        return total_requested - total_paid


class SponsorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ['full_name', 'phone', 'amount', 'progress', 'organization_name', 'sponsor_status']


class StudentaUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['full_name', 'phone_number', 'degree', 'contract_price', 'university']
