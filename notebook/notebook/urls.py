from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo.views import ProjectSpecialViewSet,ToDoModelViewSet
from users.views import UserSpecialViewSet

router = DefaultRouter()
router.register('users', UserSpecialViewSet, basename='users')
router.register('projects', ProjectSpecialViewSet, basename='projects')
router.register('todo', ToDoModelViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
