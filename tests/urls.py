
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^$', "tests.views.post_list"),
    url(r'^create/$', "tests.views.post_create"),
    url(r'^detail/$', "tests.views.post_detail"),
    url(r'^update/$', "tests.views.post_update"),
    url(r'^delete/$', "tests.views.post_delete"),
]
