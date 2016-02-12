from django.conf.urls import url

from . import views

urlpatterns = [
     # ex: /posts/

    url(r'^$', views.index, name='index'),
    url(r'^check/$', views.check, name='check'),
	url(r'^ques/$', views.ques, name='que'),
]
