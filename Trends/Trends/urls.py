"""trends URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# from main.views import index, trend_uk, trend_sa, trend_ge, trend_us
from main.views import index, trend_all

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),

    # path('trend_uk/', trend_uk, name='trend_uk'),
    # path('trend_sa/', trend_sa, name='trend_sa'),
    # path('trend_ge/', trend_ge, name='trend_ge'),
    # path('trend_us/', trend_us, name='trend_us'),
    path('trend/<str:country>', trend_all, name='trend_all'),
]