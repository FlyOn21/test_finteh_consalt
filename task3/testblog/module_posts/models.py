from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField("staff", default=False)
    is_active = models.BooleanField("active", default=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email

class Posts(models.Model):
    post_title = models.CharField(verbose_name="title", max_length=256)
    post_text = models.TextField(verbose_name="text")
    photo = models.ImageField(verbose_name="photo",upload_to="media")
    datetime = models.DateTimeField(verbose_name="datetime",auto_now=True)
    owner_user = models.CharField(verbose_name="owner", max_length=256, default="Jon Doy",blank=True)

    def __str__(self):
        return f"{self.post_title} | {self.post_text} | {self.photo} | {self.owner_user}"

class PostComments(models.Model):
    comment_text = models.TextField(verbose_name="comments")
    datetime = models.DateTimeField(verbose_name="datetime", auto_now=True)
    post_id = models.ForeignKey("Posts", on_delete=models.CASCADE)
