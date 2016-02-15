from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.index,name="index"),
    url(r'^login/', views.signup),
    url(r'^questions/', views.questions),
    url(r'^update_state/', views.update_state),
]
