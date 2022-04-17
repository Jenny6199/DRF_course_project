from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework.permissions import AllowAny
from todo.views import ProjectSpecialViewSet,ToDoSpecialViewSet
from users.views import UserSpecialViewSet, UserVersioningViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from graphene_django.views import GraphQLView

schema_view = get_schema_view(
    openapi.Info(
        title="Notebook",
        default_version='0.1',
        description="Documentation to project",
        contact=openapi.Contact(email="jenny6199@yandex.ru"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[AllowAny],  
    )


router = DefaultRouter()
router.register('users', UserSpecialViewSet, basename='users')
router.register('projects', ProjectSpecialViewSet, basename='projects')
router.register('todo', ToDoSpecialViewSet, basename='todo')


urlpatterns = [
    # Админ-панель
    path('admin/', admin.site.urls),
    # Авторизация пользователей
    path('api-auth', include('rest_framework.urls')),
    # API
    path('api/', include(router.urls)),
    # Версионирование
    # re_path(r'^api/(?P<version>\d.\d)/users/$', UserVersioningViewSet.as_view()),
    # path('api/users/0.1', include('users.urls', namespace='0.1')),
    # path('api/users/0.2', include('users.urls', namespace='0.2')),
    # path('api/users/', UserVersioningViewSet.as_view()),
    # Путь для получения токена пользователя
    path('api-token-auth/', views.obtain_auth_token),
    # Пути для получения JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # Пути для документации
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # Путь для GraphQL-запросов
    path('grahphql/', GraphQLView.as_view(graphql=True)),
]
