import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class User(models.Model):
    ROLE_CHOICES = (
        ('user', 'Oddiy foydalanuvchi'),
        ('admin', 'Admin')
    )
    full_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='F.I.Sh')
    username = models.CharField(max_length=100, null=True, blank=True, verbose_name='Username')
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default='user', null=True, blank=True,
                            verbose_name='Foydalanuvchi roli')
    telegram_id = models.BigIntegerField(null=True, blank=True, unique=True, verbose_name="Telegram ID")
    joined_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Qo'shilgan vaqti")

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Foydalanuvchilar'
        db_table = 'users'

    def __str__(self):
        return self.full_name


class FoodComment(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    table_number = models.CharField(max_length=4, null=True, blank=True, verbose_name="Stol raqami")
    grade = models.IntegerField(null=True, blank=True, validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ], verbose_name="Baho")
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True,
                                      verbose_name="Yaratilgan vaqti")

    class Meta:
        verbose_name = 'Food Comment'
        verbose_name_plural = "Taom uchun baholar"
        db_table = 'food_comment'

    def __str__(self):
        return f"{self.table_number}"


class WaiterComment(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    table_number = models.CharField(max_length=4, null=True, blank=True, verbose_name="Stol raqami")
    grade = models.IntegerField(null=True, blank=True, validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ], verbose_name="Baho")
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True,
                                      verbose_name="Yaratilgan vaqti")

    class Meta:
        verbose_name = 'Waiter Comment'
        verbose_name_plural = "Ofitsiant uchun baholar"
        db_table = 'waiter_comment'

    def __str__(self):
        return f"{self.table_number}"


class Comments(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    table_number = models.CharField(max_length=4, null=True, blank=True, verbose_name="Stol raqami")
    comment = models.TextField(null=True, blank=True, verbose_name="Komentariya")
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True,
                                      verbose_name="Yaratilgan vaqti")

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = "Komentariyalar"
        db_table = 'comment'

    def __str__(self):
        return f"{self.table_number}"
