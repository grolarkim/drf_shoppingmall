from django.db import models

from product.models import Product
from user.models import User


class Review(models.Model):
    created_at = models.DateTimeField(verbose_name="생성 시각", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정 시각", auto_now=True)
    product = models.ForeignKey(to=Product, verbose_name="상품", on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, verbose_name="사용자", on_delete=models.CASCADE)
    rating = models.IntegerField(verbose_name="평점")
    content = models.TextField(verbose_name="리뷰 내용", blank=True)
