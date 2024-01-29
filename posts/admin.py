from django.contrib import admin
from .models import Post
# Register your models here.

class productAdmin(admin.ModelAdmin):
    list_display = ['title','draft']
    list_filter = ['draft']
    search_fields = ['title']
    





admin.site.register(Post,productAdmin)
