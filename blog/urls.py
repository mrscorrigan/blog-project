from django.conf.urls import url
from django.contrib import admin
import views
urlpatterns = [
    url(r'^blog/$', views.post_list),
    # url(r'^admin/', admin.site.urls)
    url(r'^blog/(?P<id>\d+)/$', views.post_details),
]