from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('wordconfuse.views',
        (r'^$', TemplateView.as_view(template_name="index.html")),
        url(r'^get_words$', 'get_words', name='get_words'),
        url(r'^gameover$', 'gameover', name='gameover'),
        url(r'^new_hs$', 'new_hs', name='new_hs'),
        url(r'^hs$', 'hs', name='hs'),
        )
