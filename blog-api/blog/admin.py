from django.contrib import admin

# Register your models here.
from .models import Post, Notes

admin.site.register(Post)
admin.site.register(Notes)