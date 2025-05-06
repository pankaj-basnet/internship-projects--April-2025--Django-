from django.contrib import admin

from .models import Post, Tag, Comment, GroupProfile, Like

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "is_draft", "created_at")
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("sentences", "created_at", "is_approved")
    # prepopulated_fields = {"slug": ("title",)}
    list_filter = ('is_approved',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Like)
class TagAdmin(admin.ModelAdmin):
    list_display = ("post", "user",)

@admin.register(GroupProfile)
class GroupProfileAdmin(admin.ModelAdmin):
    list_display = ( "group", "description",)