"""dennisivy URL Configuration

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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    #1
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="password_reset"),

    #Where can I find OR set theses paths these values
    #2
    path('password_reset_done/', 
        auth_views.PasswordResetDoneView.as_view(template_name="email_sent.html"),name="password_reset_done"),
    #3
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset.html"), name="password_reset_confirm"),

    #4
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_complete.html"), name="password_reset_complete"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
