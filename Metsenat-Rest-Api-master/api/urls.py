from django.urls import path
from api.views import (
    RegisterAPIView,
    LoginAPIView,
    StudentSponsorAPIView,
    StudentAPIView,
    SponsorAPIView,
    AddStudentAPIView,
    PaymentSummaryAPIView,
    SponsorUpdateAPIView,
    StudentUpdateAPIView,
    SponsorFilterView,
    StudentFilterView,
    StudentSponsorFilterView
)

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('student-sponsor/', StudentSponsorAPIView.as_view(), name='studentsponsor'),
    path('student-sponsor/<int:pk>/', StudentSponsorAPIView.as_view(), name='studentsponsordetail'),
    path('student/', StudentAPIView.as_view(), name='student'),
    path('student/<int:pk>/', StudentAPIView.as_view(), name='studentdetail'),
    path('sponsor/', SponsorAPIView.as_view(), name='sponsor'),
    path('sponsor/<int:pk>/', SponsorAPIView.as_view(), name='sponsordetail'),
    path('student/add/', AddStudentAPIView.as_view(), name='addstudent'),
    path('dashboard/', PaymentSummaryAPIView.as_view(), name='dashboard'),
    path('sponsor/update/<int:pk>/', SponsorUpdateAPIView.as_view(), name='sponsorupdatedetail'),
    path('student/update/<int:pk>/', StudentUpdateAPIView.as_view(), name='studentupdatedetail'),
    path('sponsor/filter/', SponsorFilterView.as_view(), name='sponsorfilter'),
    path('student/filter/', StudentFilterView.as_view(), name='studentfilter'),
    path('student-sponsor/filter/', StudentSponsorFilterView.as_view(), name='studentsponsorfilter'),
]
