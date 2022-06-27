from django.db import models

from product.models import Product, ProductOption
from user.models import User


class Cart(models.Model):
    created_at = models.DateTimeField(verbose_name="생성 시각", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정 시각", auto_now=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="사용자")
    product_option = models.ForeignKey(to=ProductOption, on_delete=models.CASCADE, verbose_name="선택된 상품 옵션")
    count = models.IntegerField(verbose_name="수량", default=1)


class PaymentMethod(models.Model):
    created_at = models.DateTimeField(verbose_name="생성 시각", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정 시각", auto_now=True)
    name = models.CharField(verbose_name="결제 방법", max_length=100, unique=True)
    description = models.TextField(verbose_name="설명", blank=True)
    

class PurchaseList(models.Model):
    created_at = models.DateTimeField(verbose_name="생성 시각", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정 시각", auto_now=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="사용자")
    product_option = models.ForeignKey(to=ProductOption, on_delete=models.CASCADE, verbose_name="선택된 상품 옵션")
    count = models.IntegerField(verbose_name="수량", default=1)
    payment_method = models.ForeignKey(to=PaymentMethod, on_delete=models.CASCADE, verbose_name="결제 방법")
    delivery_status = models.CharField(verbose_name="배달 상황", max_length=100)
    payed_money = models.IntegerField(verbose_name="결제 금액")
    