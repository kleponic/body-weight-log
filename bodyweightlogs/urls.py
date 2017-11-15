from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^/$', views.index, name="index"),
    url(r'^create/$', views.create, name="create"),

    url(r'^detail/(?P<uuid>[0-9a-z-]+)/$', views.detail, name="detail"),
    url(r'^update/(?P<uuid>[0-9a-z-]+)/$', views.update, name="update"),

]


