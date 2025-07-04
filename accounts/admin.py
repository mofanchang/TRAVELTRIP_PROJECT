from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_staff', 'is_active')
    search_fields = ('email', 'username')

# Register your models here.
