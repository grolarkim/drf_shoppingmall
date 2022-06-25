from django.db import models

from user.models import User


class Category(models.Model):
    created_at = models.DateTimeField(verbose_name="생성 시각", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정 시각", auto_now=True)
    name = models.CharField(verbose_name="카테고리 이름", unique=True, max_length=100)
    category = models.ForeignKey(
        to="self",
        null=True,
        blank=True,
        related_name="related_category",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    created_at = models.DateTimeField(verbose_name="생성 시각", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정 시각", auto_now=True)
    thumbnail = models.ImageField(verbose_name="썸네일", upload_to="product/productimage/")
    full_image = models.ImageField(
        verbose_name="이미지", upload_to="product/productimage/"
    )


class Product(models.Model):
    created_at = models.DateTimeField(verbose_name="생성 시각", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정 시각", auto_now=True)
    user = models.ForeignKey(to=User, verbose_name="상품 판매자", on_delete=models.CASCADE)
    category = models.ManyToManyField(
        to=Category, verbose_name="카테고리", null=True, blank=True
    )
    images = models.OneToOneField(
        to=ProductImage, on_delete=models.CASCADE, blank=True, null=True
    )
    is_active = models.BooleanField(verbose_name="활성화 여부", default=True)
    title = models.CharField(verbose_name="상품 이름", max_length=100)
    description = models.TextField(verbose_name="상품 설명")

    def __str__(self):
        return self.title


class ProductOption(models.Model):
    created_at = models.DateTimeField(verbose_name="생성 시각", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정 시각", auto_now=True)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="옵션 이름", max_length=100)
    description = models.TextField(verbose_name="옵션 설명", null=True, blank=True)
    price = models.IntegerField(verbose_name="가격")

    def __str__(self):
        return f"{self.product.name}의, {self.name} 옵션"
