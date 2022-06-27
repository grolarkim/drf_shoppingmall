from django.db import models

from product.models import Product, ProductOption
from user.models import User


class Cart(models.Model):
    created_at = models.DateTimeField(verbose_name="생성 시각", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정 시각", auto_now=True)