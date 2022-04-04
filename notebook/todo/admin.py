from django.contrib import admin
from .models import Project, ToDo

class ProjectAdmin(admin.ModelAdmin):
    """
    Класс для настройки отображения модели проекта
    в админ-панели
    """
    list_display = ('project_name', 'project_URL', 'created_at', 'is_active')
    list_display_links = ('project_name',)
    search_fields = ('is_active',)
    
class ToDOAdmin(admin.ModelAdmin):
    """
     Класс для настройки отображения модели заметки
     в админ-панели
    """
    list_display = ('short_description', 'creator', 'project', 'text')
    list_display_links = ('project',)
    search_fields = ('creator',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(ToDo, ToDOAdmin)
