"""
URL configuration for online_store project.

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
from django.urls import path
from . import views


urlpatterns = [
    path('product/week/<int:consumer_id>/', views.product_week, name='week'),
    path('product/month/<int:consumer_id>/',
         views.product_month, name='month'),
    path('product/year/<int:consumer_id>/', views.product_year, name='year'),
    path('postproduct/', views.post_product, name='postproduct'),
    path('upload/', views.upload_image, name='upload_image'),
    path('upload_base/<int:product_id>/',
         views.upload_image_base, name='upload_image_base'),

]
