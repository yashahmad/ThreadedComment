from django.contrib import admin
from .models import Page, Comment, Subcomment

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('id','name','created','updated')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','name','created','updated','page_id')

@admin.register(Subcomment)
class SubcommentAdmin(admin.ModelAdmin):
    list_display = ('id','name','created','updated','comment_id')
