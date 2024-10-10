from django.contrib import admin
from .models import Post


# register post model in admin interface
admin.site.register(Post)