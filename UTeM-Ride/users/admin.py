from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'user_type', 'is_verified_driver', 'is_active')
    list_filter = ('user_type', 'is_verified_driver', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('UTeM Ride Info', {
            'fields': ('user_type', 'is_verified_driver', 'student_id', 'license_number', 'phone_number')
        }),
    )