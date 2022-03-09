from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo.serializers import ProjectModelSerializer
from todo.views import ProjectModelViewSet, ToDoModelViewSet, ProjectAPIVIew
from users.views import UserModelViewSet

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('projects', ProjectModelViewSet)
router.register('todo', ToDoModelViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('views/api-view/', ProjectAPIVIew.as_view()),
]
