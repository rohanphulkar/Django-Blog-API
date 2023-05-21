from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView

app_name = 'accounts'

urlpatterns = [
    # Endpoint for user registration
    path("register/",views.RegistrationAPIView.as_view(),name="register"),

    # Endpoint for user login and token retrieval
    path("login/",TokenObtainPairView.as_view(),name="login"),
    
    # Endpoint for email verification with verification code
    path("verify/<verification_code>/",views.EmailVerificationView.as_view(),name="email_verification"),
]