from api.models import User
from api.serializers import RegisterSerializer, LoginSerializer
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import permissions
from rest_framework.response import Response
from .models import University, Student, Sponsor, StudentSponsor
from .serializers import (
    UserSerializer, UniversitySerializer, StudentSerializer,
    SponsorSerializer, StudentSponsorSerializer
)


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save(password=make_password(serializer.validated_data['password']))

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response({
                'refresh': str(refresh),
                'access': access_token,
                'username': serializer.data
            }, status=status.HTTP_201_CREATED
            )

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            user = User.objects.get(email=email)
            if user.check_password(password):
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)

                return Response({'refresh': str(refresh), 'access': str(access_token)},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'detail': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserMeAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


# University API
class UniversityAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        universities = University.objects.all()
        serializer = UniversitySerializer(universities, many=True)
        return Response(serializer.data)


# Student API
class StudentAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


# Sponsor API
class SponsorAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        sponsors = Sponsor.objects.all()
        serializer = SponsorSerializer(sponsors, many=True)
        return Response(serializer.data)


# Student-Sponsor Relationship API
class StudentSponsorAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        student_sponsors = StudentSponsor.objects.all()
        serializer = StudentSponsorSerializer(student_sponsors, many=True)
        return Response(serializer.data)
