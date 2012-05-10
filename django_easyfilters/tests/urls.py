# URLs to make it easy to add more data for the test suite.
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^books/', 'django_easyfilters.tests.views.books'),
    url(r'^authors/', 'django_easyfilters.tests.views.authors'),
    url(r'^admin/', include(admin.site.urls)),
)
