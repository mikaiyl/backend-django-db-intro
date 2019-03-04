"""db_demo URL Configuration

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
from django.urls import path

from db_demo.models import *

admin.site.register(Permission)
admin.site.register(Profile)
admin.site.register(Contributor)
admin.site.register(Category)
admin.site.register(Role)
admin.site.register(Tag)
admin.site.register(Page)

urlpatterns = [
    path('admin/', admin.site.urls),
]
