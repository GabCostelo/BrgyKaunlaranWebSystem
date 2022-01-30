"""BrgySystem_WebBased URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/password_reset/', auth_views.PasswordResetView.as_view(),name='admin_password_reset'),
    path('',views.index,name='home'),
    path('accounts/',include('accounts.urls',namespace='accounts')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('staff/',include('staffPage.urls',namespace='staff')),
    path('staff/',include('django.contrib.auth.urls')),
    path('events/',include('post.urls',namespace='post')),
    path('events/',include('django.contrib.auth.urls')),
    path('docu_Request/',include('documentRequest.urls',namespace='docuRequest')),
    path('docu_Request/',include('django.contrib.auth.urls')),
    path('records/',include('records.urls',namespace='records')),
    path('records/',include('django.contrib.auth.urls')),
    path('aboutus/',views.aboutus,name='about'),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
