"""
URL configuration for Fefilov project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Alexandr import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.res, name='res', kwargs={'name': 'Alexandr','surname': 'Fefilov', 'age': '16 y.o.','interes':'PC games and makaroni'}),
    path('about/', views.about, name='about', kwargs={'place':'Zavyalovo', 'uspev': 'Udarnik', 'learning': 'like learning'}),
    path('contact/',views.contact, name='contact', kwargs={'github':'Batla510', 'tg': '89911974606', 'vk': '@pumpda','discord':'kulebaka7230'})
]
