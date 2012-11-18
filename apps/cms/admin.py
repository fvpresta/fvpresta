# coding=utf8

from django.contrib import admin
from apps.cms.models import Client, Project, Capture
from easy_thumbnails.files import get_thumbnailer

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'logoView')

    def logoView(self, obj):
        logo_url = get_thumbnailer(obj.logo)['logo_small'].url
        return '<img src="%s" title="%s" />' % (logo_url, obj.name)
    logoView.short_description = 'Logo'
    logoView.allow_tags = True
admin.site.register(Client, ClientAdmin)

class ProjectAdmin(admin.ModelAdmin):
    class CaptureInline(admin.TabularInline):
        model = Capture
        max_num = 10
        extra = 1

    inlines = (CaptureInline,)
admin.site.register(Project, ProjectAdmin)