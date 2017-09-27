from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        r'^$',
        views.StatListView.as_view(),
        name='stat_list'
    ),
    url(
        r'^create/$',
        views.StatCreateView.as_view(),
        name='stat_create'
    ),
    url(
        r'^(?P<pk>[\d]+)/$',
        views.StatDetailView.as_view(),
        name='stat_detail'
    ),
    url(
        r'^(?P<pk>[\d]+)/update/$',
        views.StatUpdateView.as_view(),
        name='stat_update'
    ),
    url(
        r'^(?P<pk>[\d]+)/delete/$',
        views.StatDeleteView.as_view(),
        name='stat_delete',
    ),
]
