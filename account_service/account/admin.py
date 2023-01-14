from django.contrib import admin
from .models import Account

# Register your models here.
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    """Account admin registration"""
    empty_value_display = "-empty-"
