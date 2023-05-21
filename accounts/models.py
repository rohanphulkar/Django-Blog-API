from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
import uuid
from .manager import UserManager
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse

class User(AbstractBaseUser,PermissionsMixin):
    id = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True)
    name = models.CharField(max_length=255,blank=True)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=255,null=True,blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
    
    # Sends a verification email to the user with the verification code.
    def send_verification_code(self,code,email):
        url = f"http://localhost:8000{reverse('accounts:email_verification',args=[code])}"
        send_mail(
            "Verify Your Email Address",
            f"Please verify your email address by clicking the link below:\n\n{url}\n\nThank you",
            settings.EMAIL_HOST_USER,
            [email]
        )

    # Overrides the default save method to generate a verification code and send a verification email
    # if the user is not already verified.
    def save(self, *args, **kwargs):
        if not self.is_verified:
            code = str(uuid.uuid4())
            self.verification_code = code
            self.send_verification_code(code, self.email)
        super().save(*args, **kwargs)

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
            return self.is_admin

    def has_module_perms(self, app_label):
            return self.is_admin