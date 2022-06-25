from django.db import models


class Category(models.Model):
    created_at = models.DateTimeField(verbose_name="생성 시각", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정 시각", auto_now=True)
    name = models.CharField(verbose_name="카테고리 이름", unique=True, max_length=100)
    category = models.ForeignKey(to="self", null=True, blank=True, related_name="related_category", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

