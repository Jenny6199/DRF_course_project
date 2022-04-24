from django.urls import path
from .views import UserVersioningViewSet

app_name = 'users'

urlpatterns = [
    path('', UserVersioningViewSet.as_view()),
]
