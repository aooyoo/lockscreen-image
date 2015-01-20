from django.contrib import admin

from apps.phone.models import Phone

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('udid', 'phone', 'first_login', 'last_login')
