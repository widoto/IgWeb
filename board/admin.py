from django.contrib import admin
from .models import Board, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Board)
class BoardAdmin(SummernoteModelAdmin):
    summernote_fields = ('contents',)
    list_display = (
        'title',
        'contents',
        'writer',
        'sentence',
        'board_name',
        'hits',
        'write_dttm',
        'update_dttm',
        'image',
        'file'
    )
    list_display_links = list_display

admin.site.register(Comment)