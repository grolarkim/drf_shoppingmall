from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("Users must have an username")
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username=username, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(verbose_name="유저 아이디", max_length=100, unique=True)
    password = models.CharField(verbose_name="비밀번호", max_length=128)
    fullname = models.CharField(verbose_name="사용자 이름", max_length=100)
    phone_number = models.CharField(verbose_name="전화번호", max_length=30)
    email = models.EmailField(verbose_name="이메일", max_length=128)
    created_at = models.DateTimeField(verbose_name="가입 시각", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정 시각", auto_now=True)
    is_active = models.BooleanField(verbose_name="활성화 여부", default=True)
    is_admin = models.BooleanField(verbose_name="관리자 여부", default=False)
    is_seller = models.BooleanField(verbose_name="판매자 여부", default=False)

    @property
    def is_staff(self):
        return self.is_admin

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
