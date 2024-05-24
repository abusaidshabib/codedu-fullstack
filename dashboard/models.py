from django.db import models
from django.utils.translation import gettext as _
from django.utils.text import slugify

from clientapp.models import BaseModel

# Create your models here.

LEVEL_OPTION = [
    ('B', 'Beginner'),
    ('I', 'Intermediate'),
    ('A', 'Advance')
]

class Topic(models.Model):
    name = models.CharField(_("course Topics"), max_length=100)

class Courses(BaseModel):

    title = models.CharField(_("Course Title"), max_length=200)
    level = models.CharField(_("Course Level"), max_length=50, choices=LEVEL_OPTION, default='B')
    duration = models.CharField(_("Course Duration"), max_length=10)
    description = models.TextField(_("Course Description"))
    topics = models.ManyToManyField(Topic, verbose_name=_("Course Topics"))
    price = models.FloatField(_("Course Price"))
    slug = models.SlugField(blank=True, max_length=80, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
