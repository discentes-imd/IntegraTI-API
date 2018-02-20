from django.db import models
from django.contrib.auth.models import AbstractUser


class Base(models.Model):
    is_active = models.BooleanField(default=False)

    inserted_since = models.DateField(auto_now_add=True)
    inserted_by = models.ForeignKey('User', related_name="entries_inserted", null=True, on_delete=models.PROTECT)

    last_updated_since = models.DateField(auto_now=True)
    updated_by = models.ForeignKey('User', related_name="entries_updated", null=True, on_delete=models.PROTECT)

    class Meta:
        abstract = True


class User(AbstractUser, Base):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

