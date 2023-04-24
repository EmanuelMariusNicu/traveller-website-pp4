from django.contrib import admin
from .models import Trip, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Trip)
class TripAdmin(SummernoteModelAdmin):
    """
    Admin for Trip model
    """
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = 'content'
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin for Comment model 
    """
    list_display = ('name', 'body', 'post', 'approved', 'created_on')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comment']

    def approve_comment(self, request, queryset):
        queryset.update(approved=True)
