from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from todo.views import ProjectSpecialViewSet,ToDoSpecialViewSet
from users.views import UserSpecialViewSet

router = DefaultRouter()
router.register('users', UserSpecialViewSet, basename='users')
router.register('projects', ProjectSpecialViewSet, basename='projects')
router.register('todo', ToDoSpecialViewSet, basename='todo')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    # Путь для получения токена пользователя
    path('api-token-auth/', views.obtain_auth_token)
]
