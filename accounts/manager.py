from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have a password')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)

        user.save()
        return user

    def create_superuser(self, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        # Create a regular user using the create_user method
        user = self.create_user(
            email=email,
            password=password,
        )

        
        # Set additional fields for the superuser
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_verified = True

        # save the superuser object
        user.save()
        return user