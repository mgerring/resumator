from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import DetailView
from resume.data.models import *
from resume.data.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^resumine/', include('resumine.foo.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
	(r'^resume/(?P<pk>\d)/$', DetailView.as_view(model=ResumeVersion, template_name='resume.html')),
	(r'^resume/(?P<resume_id>\d).json/$', 'resume.data.views.resume_as_json'),
)
urlpatterns += staticfiles_urlpatterns()