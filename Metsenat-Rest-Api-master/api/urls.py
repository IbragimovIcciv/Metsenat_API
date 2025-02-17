from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from api.views import RegisterAPIView, LoginAPIView, UserAPIView, UserMeAPIView, UniversityAPIView, StudentAPIView, \
    SponsorAPIView, StudentSponsorAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('users/', UserAPIView.as_view(), name='user-list'),
    path('users/me/', UserMeAPIView.as_view(), name='user-me'),
    path('universities/', UniversityAPIView.as_view(), name='university-list'),
    path('students/', StudentAPIView.as_view(), name='student-list'),
    path('sponsors/', SponsorAPIView.as_view(), name='sponsor-list'),
    path('student-sponsors/', StudentSponsorAPIView.as_view(), name='student-sponsor-list'),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
