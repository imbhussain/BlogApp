from django.contrib import admin
from .models import Post,Contact
# Register your models here.
admin.site.register([Post,Contact])

admin.site.site_header='Site Administration'
