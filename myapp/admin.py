from django.contrib import admin
from .models import Posts
# Register your models here.

admin.site.register(Posts)


class Admin(admin.ModelAdmin):
    list_display=["title"]
    
