"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
#  to display the image in the website
from django.conf import settings
from django.conf.urls.static import static
from olx import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('add/',views.register_vehicle,name="add"),
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name="login"),
    path('details/<int:n>/',views.details,name="details"),
    path('logout/', views.user_logout, name="logout"),
    path('edit/<int:d>/',views.edit,name="edit"),
    path('delete/<int:d>/',views.delete,name="delete"),
]
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)