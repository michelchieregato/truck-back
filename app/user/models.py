from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    """
    This class extends the BaseUserManager, allowing us to customize the user
    fields and creation methods.
    """
    use_in_migrations = True

    def _validate_fields(self, email):
        if not email:
            raise ValueError('Email address is required')

    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a new User
        """
        self._validate_fields(email)
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_super_user(self, email, password=None, **extra_fields):
        self._validate_fields(email)
        user = self.model(email=self.normalize_email(email), is_superuser=True, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model that inherits AbstractBaseUser, so we can apply customizations.
    It supports using email instead of username.
    """
    USERNAME_FIELD = 'email'

    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.')
    is_superuser = models.BooleanField(default=False, help_text='Designates whether the user can delete and create objects in admin site.')
    is_active = models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. '
                                                            'Unselect this instead of deleting accounts.')
    points = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return self.name