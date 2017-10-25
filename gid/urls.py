from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.glav, name='glav'),
    #url(r'^ot/new/$', views.ot_new, name='ot_new'),
   # url(r'^ot/',views.ot_list, name='ot_list'),
    url(r'^tyrs/(?P<pk>\d+)/$', views.tyr_detail, name='tyr_detail'),
    url(r'^tyrs/new/$', views.tyr_new, name='tyr_new'),
    url(r'^tyrs/(?P<pk>\d+)/ot/$', views.ot_new, name='ot_new'),
    url(r'^tyrs/', views.tyrs, name='tyrs'),
    url(r'^about/', views.about, name='about'),
    url(r'^images/', views.images, name='images'),
      ]