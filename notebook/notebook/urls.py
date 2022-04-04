from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from todo.views import ProjectSpecialViewSet,ToDoSpecialViewSet
from users.views import UserSpecialViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

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
    # Путь для получения токена пользователя
    path('api-token-auth/', views.obtain_auth_token),
    # Пути для получения JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
