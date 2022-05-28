from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class ArticleUserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class ArticleUser(AbstractBaseUser, PermissionsMixin):
    USER = 'subscriber'
    AUTHOR = 'author'

    ROLES = [
        (USER, 'Subscriber'),
        (AUTHOR, 'Author'),
    ]

    username = models.CharField(max_length=100, unique=False, blank=True)
    role = models.CharField(max_length=100, choices=ROLES, default=USER)
    email = models.EmailField(blank=False, unique=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = ArticleUserManager()
