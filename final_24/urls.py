"""final_24 URL Configuration

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
# from django.conf.urls import url
# from django.contrib import admin
# from Application1 import views

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^s1/', views.sample1,name='web3'),
#     url(r'^a3/', views.sample3),
#     url(r'^s3/', views.sample3,name='web1'),
    
# ]













from django.urls import path
from Application1 import views

urlpatterns = [
    path('main/', views.sample3, name='web3'),  
    path('register/', views.sample1, name='web1'),  
]
