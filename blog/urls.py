# Imported admin, path, settings & static 
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Imported View functions from blog app

from blogapp.views import index,detail,create_post,update_post,delete_post,log_in,log_out,aboutus,contactus
#Created Urls for functions
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
]+ static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # Appended media URL & media root for images
