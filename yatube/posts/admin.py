from django.contrib import admin

from .models import Group, Post


class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'description'
    )
    search_fields = ('title',)
    list_filter = ('title', 'slug',)
    empty_value_display = '-пусто-'


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
    search_fields = ('text',)
    list_editable = ('group',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Group, GroupAdmin)
admin.site.register(Post, PostAdmin)
