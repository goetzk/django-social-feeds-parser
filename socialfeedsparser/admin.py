from django.contrib import admin
from django.template.defaultfilters import truncatewords
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from django.utils.html import format_html

from .models import Post, Channel


def get_messages(modeladmin, request, queryset):
    """
    Collects messages from selected sources.
    """
    for source in queryset:
        sc = source.source_class(channel=source)
        sc.collect_messages()
        source.updated = now()
        source.save()

get_messages.short_description = _('Get Messages from selected sources')


class ChannelAdmin(admin.ModelAdmin):
    """
    Admin class for the Channel model.
    """
    list_display = ('query', 'name', 'source', 'query_type', 'updated', 'is_active', 'show_linkedin_token_renew_link')
    list_filter = ('query', 'source', 'query_type', 'updated', 'is_active')
    # exclude = ('user_secret', 'user_token',)
    exclude = ('user_secret', )
    actions = [get_messages]
    radio_fields = {"query_type": admin.HORIZONTAL}

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj=obj)
        if obj and obj.source == 'instagram':
            readonly_fields += ('user_token', )
        return readonly_fields

    def show_linkedin_token_renew_link(self, obj):
        return format_html('<a href="%s">%s</a>' % (obj.token_renew_link, _('Click to renew'))) if obj.source == 'linkedin' else ''
    # show_linkedin_token_renew_link.allow_tags = True  # deprecated from Django 1.9.
    show_linkedin_token_renew_link.short_description = _('Renew Token')


class PostAdmin(admin.ModelAdmin):
    """
    Admin class for the Post model.
    """
    list_display = ('channel', 'author', 'content_admin', 'date',
                    'is_active', 'order')
    list_filter = ('is_active', 'channel')
    list_editable = ('is_active', 'order', 'author', 'date')

    def content_admin(self, obj):
        return truncatewords(obj.content, 20)
    content_admin.short_description = _('Post content')


admin.site.register(Channel, ChannelAdmin)
admin.site.register(Post, PostAdmin)
