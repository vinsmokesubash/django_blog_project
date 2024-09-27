from django.contrib import admin
from .models import Posts, Category, AboutUs
# Register your models here.


class PostsAdmin(admin.ModelAdmin):
    list_display = ["title", "content"]
    search_fields = ["title"]
    list_filter = ("category", "created_at")
    
admin.site.register(Posts, PostsAdmin)
admin.site.register(Category)
admin.site.register(AboutUs)