"""blog URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static

from blogapp.views import index,detail,create_post,update_post,delete_post,log_in,log_out,aboutus,contactus
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('detail/<int:id>',detail,name='detail'),
    path('blogpost/',create_post,name="blogpost"),
    path('updatepost/<int:id>',update_post,name="update_post"),
    path('deletepost/<int:id>',delete_post,name="delete_post"),
    path('login/',log_in,name='log_in'),
    path('logout/',log_out,name='log_out'),
    path('about/',aboutus,name="aboutus"),
    path('contact/',contactus,name="contactus")
]+ static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
