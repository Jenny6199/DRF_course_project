from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    """
    Класс для настройки отображения модели пользователя
    в админ панели
    """
    list_display = ('username', 'email', 'is_active', 'role')
    list_display_links = ('username',)
    search_fields = ('role',)

admin.site.register(User, UserAdmin)
