from django.db import models

from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager

class User(AbstractBaseUser):
    nickname_validator = ASCIIUsernameValidator()
    firstname = models.CharField(
        verbose_name="first name",
        max_length=150
    )
    lastname = models.CharField(
        verbose_name="last name",
        max_length=150
    )
    nickname = models.CharField(verbose_name="nickname", max_length=150, unique=True, null=True)
    date_of_birth = models.DateField(null=True)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255, unique=True,
        null=False,
        blank=False,
        help_text=_(
            "Required. Enter a valid email address."
        ),
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(verbose_name="joined date", default=timezone.now)

    USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = []
    # REQUIRED_FIELDS = ["date_of_birth"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return True

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Course(models.Model):
    instructor = models.CharField(max_length=60)
    title = models.CharField(max_length=150, unique=True)
    rating = models.FloatField()
    enrolled = models.BigIntegerField()