from django.contrib import admin
from .models import Post,Contact

# Models (Post & Contact) registered here.
admin.site.register([Post,Contact])

admin.site.site_header='Site Administration' # Admin dashboard site title edited 
