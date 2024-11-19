from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.translation import gettext_lazy as _

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'phone', 'direction', 'group') # Ro'yxatda ko'rsatiladigan ustunlar
    list_filter = ('is_staff', 'is_superuser', 'groups') # Filtrlash qismi
    search_fields = ('username', 'first_name', 'last_name', 'phone') # Qidirish qismi
    ordering = ('username',) # Tartiblash tartibi
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_("Shaxsiy ma'lumotlar"), {'fields': ('first_name', 'last_name', 'patronymic', 'phone', 'direction', 'group')}),
        (_('Ruxsatlar'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Muhim sanalar'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )

