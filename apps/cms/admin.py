# coding=utf8

from django.contrib import admin
from apps.cms.models import Client, Project, Capture, Carousel
from easy_thumbnails.files import get_thumbnailer

class ClientAdmin(admin.ModelAdmin):
    list_display = ('display_order', 'name', 'url', 'logoThumb')
    list_display_links = ('name',)
    list_editable = ('display_order',)

    def logoThumb(self, obj):
        logo_url = get_thumbnailer(obj.logo)['logo_small'].url
        return '<img src="%s" title="%s" />' % (logo_url, obj.name)
    logoThumb.short_description = 'Logo'
    logoThumb.allow_tags = True
admin.site.register(Client, ClientAdmin)

class ProjectAdmin(admin.ModelAdmin):
    class CaptureInline(admin.TabularInline):
        model = Capture
        max_num = 10
        extra = 1

    inlines = (CaptureInline,)
admin.site.register(Project, ProjectAdmin)

class CarouselAdmin(admin.ModelAdmin):
    list_display = ('carouselThumb',)

    def carouselThumb(self, obj):
        carousel_url = get_thumbnailer(obj.image)['carousel_small'].url
        return '<img src="%s" />' % (carousel_url)
    carouselThumb.short_description = 'Carousel'
    carouselThumb.allow_tags = True
admin.site.register(Carousel, CarouselAdmin)