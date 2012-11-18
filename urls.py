from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

# CMS
urlpatterns += patterns('apps.cms.views',
    url(r'^$',         'home',      name = 'cms_home'),
    url(r'^about_us',  'aboutUs',   name = 'cms_about_us'),
    url(r'^clients',   'clients',   name = 'cms_clients'),
    url(r'^portfolio', 'portfolio', name = 'cms_portfolio'),
    url(r'^contact',   'contact',   name = 'cms_contact'),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
