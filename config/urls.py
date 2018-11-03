"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('account.urls')),
    path('api/v1/', include('gallery.urls')),
    path('admin/', admin.site.urls),
]

# Api url docs onlu available on development
# and we only add midea url in development
# once we deploy we'll use nginx to handle all static files
if settings.DEBUG:
    from django.conf.urls.static import static
    from rest_framework.documentation import include_docs_urls

    urlpatterns = [
        path('api/v1/docs/', include_docs_urls()),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
