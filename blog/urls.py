from django.conf.urls import url
from django.contrib import admin
import views
from blog_prj.settings import MEDIA_ROOT
from . import views
from .forms import BlogPostForm

urlpatterns = [
    url(r'^$', views.post_list),
    # url(r'^admin/', admin.site.urls)
    url(r'^(?P<id>\d+)/$', views.post_details, name='post_detail'),
    url(r'^post/new/$',views.new_post,name='new_post'),

]