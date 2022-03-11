from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo.serializers import ProjectModelSerializer
from todo.views import ProjectCreateAPIView, ProjectCustomViewSet, ProjectDestroyAPIView, ProjectDjangoFilterViewSet, ProjectKwargsFilterView, ProjectListAPIView, ProjectModelViewSet, ProjectParamFilterViewSet, ProjectQuerysetFilterViewSet, ProjectRetrieveAPIView, ProjectUpdateAPIView, ToDoModelViewSet, ProjectAPIVIew
from todo.views import ProjectViewSet
from users.views import UserModelViewSet

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('projects', ProjectModelViewSet)
# router.register('projects', ProjectQuerysetFilterViewSet)
# router.register('projects', ProjectDjangoFilterViewSet)

# router.register('project_custom', ProjectCustomViewSet)
router.register('todo', ToDoModelViewSet)
# router.register('base', ProjectViewSet, basename='project')
# Фильтрация.

filter_router = DefaultRouter()
filter_router.register('param', ProjectParamFilterViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('views/api-view/', ProjectAPIVIew.as_view()),
    # generic CRUD for project
    path('generic/project/create/', ProjectCreateAPIView.as_view()),
    path('generic/project/list/', ProjectListAPIView.as_view()),
    path('generic/project/retrieve/<int:pk>/', ProjectRetrieveAPIView.as_view()),
    path('generic/project/update/<int:pk>/', ProjectUpdateAPIView.as_view()),
    path('generic/project/delete/<int:pk>/', ProjectDestroyAPIView.as_view()),
    # ViewSets
    path('viewsets/', include(router.urls)),
    path('viewsets/projects/filter/kwargs/<str:project_name>/', ProjectKwargsFilterView.as_view()),
    # Filtering
    path('filters/', include(filter_router.urls)),
]
