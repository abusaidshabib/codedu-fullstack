from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.utils.text import slugify

from .managers import CustomUserManager

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class UserModel(AbstractBaseUser, BaseModel):
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

class TopicModel(models.Model):
    name = models.CharField(_("course Topics"), max_length=100)

class CourseModel(models.Model):
    title = models.CharField(max_length=150, unique=True)
    instructor = models.ManyToManyField(UserModel)
    description = models.TextField()
    LEVEL_OPTIONS = [
        ('B', _('Beginner')),
        ('I', _('Intermediate')),
        ('A', _('Advanced')),
    ]
    level = models.CharField(_("Level"), max_length=50, choices=LEVEL_OPTIONS, default='B')
    topics = models.ManyToManyField(TopicModel, verbose_name=_("Course Topics"), blank=True)
    price = models.FloatField(_("Course Price"))
    slug = models.SlugField(blank=True, max_length=80, unique=True)
    duration = models.IntegerField(_("Course Duration"))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)

    def __str__(self):
        return self.title

class LessonModel(BaseModel):
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    title = models.CharField(_(""), max_length=150)
    content = models.TextField(_(""))

    def __str__(self):
        return self.title