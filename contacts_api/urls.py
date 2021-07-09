"""contacts_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os

from django.contrib import admin
from django.urls import path, include

from varejao.urls import router as VarejaoRouter
from macapa.urls import router as MacapaRouter


admin.site.site_header = os.getenv("SITE_HEADER")
admin.site.site_title = os.getenv("SITE_TITLE")
admin.site.index_title = os.getenv("INDEX_TITLE")
admin.site.site_url = os.getenv("SITE_URL")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('auth/', include('rest_framework.urls')),
    path('api/v1/', include(('core.urls',
                             'core'), namespace='core')),
    path('api/v1/', include((VarejaoRouter.urls,
                             'varejao'), namespace='varejao')),
    path('api/v1/', include((MacapaRouter.urls,
                             'macapa'), namespace='macapa')),
]
