from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 				'app.views.home', 			name='home'),    
    url(r'^process_link/', 	'app.views.process_link', 	name='process_link'),
    url(r'^process_board/', 'app.views.process_board', 	name='process_board'),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()