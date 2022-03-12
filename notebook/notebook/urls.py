from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo.serializers import ProjectModelSerializer
from todo.views import ProjectCreateAPIView, ProjectCustomViewSet, ProjectDestroyAPIView, ProjectDjangoFilterViewSet, ProjectKwargsFilterView, ProjectLimitOffsetPaginationViewSet, ProjectListAPIView, ProjectParamFilterViewSet, ProjectQuerysetFilterViewSet, ProjectRetrieveAPIView, ProjectUpdateAPIView, ToDoModelViewSet, ProjectAPIVIew
from todo.views import ProjectViewSet
from users.views import UserSpecialViewSet

router = DefaultRouter()
router.register('users', UserSpecialViewSet)
router.register('projects', ProjectLimitOffsetPaginationViewSet)
router.register('todo', ToDoModelViewSet)

# router.register('projects', ProjectQuerysetFilterViewSet)
# router.register('projects', ProjectDjangoFilterViewSet)
# router.register('project_custom', ProjectCustomViewSet)
# router.register('base', ProjectViewSet, basename='project')
# router.register('projects/paginator', ProjectLimitOffsetPaginationViewSet)

filter_router = DefaultRouter()
# filter_router.register('param', ProjectParamFilterViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('views/api-view/', ProjectAPIVIew.as_view()),

    # Generic CRUD for project
    path('generic/project/create/', ProjectCreateAPIView.as_view()),
    path('generic/project/list/', ProjectListAPIView.as_view()),
    path('generic/project/retrieve/<int:pk>/', ProjectRetrieveAPIView.as_view()),
    path('generic/project/update/<int:pk>/', ProjectUpdateAPIView.as_view()),
    path('generic/project/delete/<int:pk>/', ProjectDestroyAPIView.as_view()),

    # Use ViewSets
    # path('viewsets/', include(router.urls)),

    # Filtrations
    path('viewsets/projects/filter/kwargs/<str:project_name>/', ProjectKwargsFilterView.as_view()),
    path('filters/', include(filter_router.urls)),
]
