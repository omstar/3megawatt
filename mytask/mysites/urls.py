from django.conf.urls import url
from mysites import views

urlpatterns = [
    url(r'^sites/$', views.ListMySites.as_view(), name='mysites-list'),
    url(r'^sites/(?P<pk>\d+)/$', views.MySiteDetail.as_view(), name='site-detail'),
    url(r'^summary/$', views.ListMySitesSum.as_view(), name='mysites-summary sum'),
    url(r'^summary-average/$', views.ListMySitesAvg.as_view(), name='mysites-summary avg'),
]
