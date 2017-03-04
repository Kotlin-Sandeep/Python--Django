from django.conf.urls import include, url
from login.views import *
 
urlpatterns = (
    url(r'^$', 'views.login'),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', 'views.login'),
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^home/$', home),
)
