from django.contrib import admin
from .models import Post,Comment,Tag
# Register your models here.
admin.site.register(Post)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

    def __str__(self):
        return self.name
