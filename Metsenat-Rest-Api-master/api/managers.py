from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, username, password, **extra_fields):
        """
        Creates and saves a User with the given email, username, and password.
        """
        if not email:
            raise ValueError('The given email must be set')

        if not username:
            raise ValueError('The given username must be set')

        email = self.normalize_email(email)

        # Check if a user with the same email or username already exists
        if self.model.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists.")

        if self.model.objects.filter(username=username).exists():
            raise ValidationError("A user with this username already exists.")

        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password=None, **extra_fields):
        """
        Creates a regular user.
        """
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)  # Ensure regular users can't access admin
        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, email, username, password, **extra_fields):
        """
        Creates a superuser with admin privileges.
        """
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)  # Allow superuser access to Django Admin

        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True.')

        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True.')  # Extra validation

        return self._create_user(email, username, password, **extra_fields)
