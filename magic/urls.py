from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        r'^$',
        views.CardSetListView.as_view(),
        name='card_set_list'
    ),
    url(
        r'^card-set/(?P<pk>[\d]+)/$',
        views.CardSetDetailView.as_view(),
        name='card_set_detail',
    ),
    url(
        r'^card/(?P<pk>[\d]+)/$',
        views.CardDetailView.as_view(),
        name='card_detail',
    ),
    url(
        r'^card-set/(?P<pk>[\d]+)/vote$',
        views.CardSetVoteRedirectView.as_view(),
        name='card_set_vote_redirect',
    ),
    url(
        r'^doto/$',
        views.doto_redirect,
        name='doto',
    ),
]
