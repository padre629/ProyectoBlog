from django.conf.urls import patterns, include, url
#import views
from blog.views import index_view, login_view, registro_view
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ProyectoBlog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #admin
    url(r'^admin/', include(admin.site.urls)),

    #index
    url(r'^$', index_view), 
    url(r'^login/$', login_view),
    url(r'^registro/$', registro_view),
)

#allow processing of all files in /media 
from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 
            'django.views.static.serve', 
            {'document_root': settings.MEDIA_ROOT}
        ),
    )
