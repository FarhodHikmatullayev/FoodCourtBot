from django.contrib import admin
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'username', 'role', 'joined_at')
    list_filter = ('joined_at', 'role')
    search_fields = ('full_name', 'username')
    date_hierarchy = 'joined_at'


@admin.register(FoodComment)
class FoodCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'table_number', 'grade', 'created_at')
    list_filter = ('created_at', 'grade')
    search_fields = ('user__full_name', 'table_number')
    date_hierarchy = 'created_at'


@admin.register(WaiterComment)
class WaiterCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'table_number', 'grade', 'created_at')
    list_filter = ('created_at', 'grade')
    search_fields = ('user__full_name', 'table_number')
    date_hierarchy = 'created_at'


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'table_number', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__full_name', 'table_number')
    date_hierarchy = 'created_at'
