from django.conf.urls.defaults import patterns, include, url
from helloworld.views import hello
urlpatterns = patterns('',
	(r,^$',hello),
)
