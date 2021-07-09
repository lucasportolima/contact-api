from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import MyTokenObtainPairView

# Swagger configuration
schema_view = get_schema_view(
    openapi.Info(
        title="Contacts API",
        default_version='v1',
        description="Contacts API documentation",
        contact=openapi.Contact(email="lucasportolima@live.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('docs/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path(
        'auth/obtain_token/',
        MyTokenObtainPairView.as_view(),
        name='auth-token'),
    path('auth/refresh_token/', TokenRefreshView.as_view(),
         name='token_refresh')
]
