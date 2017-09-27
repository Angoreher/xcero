from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        r'^$',
        views.VoteListView.as_view(),
        name='vote_list'
    ),
    url(
        r'^create/$',
        views.VoteCreateView.as_view(),
        name='vote_create'
    ),
    url(
        r'^(?P<pk>[\d]+)/$',
        views.VoteDetailView.as_view(),
        name='vote_detail'
    ),
    url(
        r'^(?P<pk>[\d]+)/update/$',
        views.VoteUpdateView.as_view(),
        name='vote_update'
    ),
    url(
        r'^(?P<pk>[\d]+)/delete/$',
        views.VoteDeleteView.as_view(),
        name='vote_delete',
    ),
]
