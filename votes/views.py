# -*- coding: utf-8 -*-
""" Views for the votes application. """
# standard library

# django
from django.core.urlresolvers import reverse

# models
from .models import Vote

# views
from base.views import BaseCreateView
from base.views import BaseDeleteView
from base.views import BaseDetailView
from base.views import BaseListView
from base.views import BaseUpdateView
from base.views import BaseRedirectView

# forms
from .forms import VoteForm

# utils
from magic.utils import get_random_card


class VoteRedirectView(BaseRedirectView):

    def get_redirect_url(self, *args, **kwargs):
        unvoted_cards = Vote.get_not_voted_cards(self.request.user)
        card_pk = get_random_card(unvoted_cards).pk

        return reverse('card_detail', args=[card_pk])


class VoteListView(BaseListView):
    """
    View for displaying a list of votes.
    """
    model = Vote
    template_name = 'votes/list.pug'
    permission_required = 'votes.view_vote'


class VoteCreateView(BaseCreateView):
    """
    A view for creating a single vote
    """
    model = Vote
    form_class = VoteForm
    template_name = 'votes/create.pug'
    permission_required = 'votes.add_vote'

    def get_success_url(self, *args, **kwargs):
        card_set_id = self.request.POST.get('card_set_id')
        return reverse('card_set_vote_redirect', args=[card_set_id])


class VoteDetailView(BaseDetailView):
    """
    A view for displaying a single vote
    """
    model = Vote
    template_name = 'votes/detail.pug'
    permission_required = 'votes.view_vote'

    def get_context_data(self, **kwargs):
        context = super(VoteDetailView, self).get_context_data(**kwargs)
        context['form'] = VoteForm()


class VoteUpdateView(BaseUpdateView):
    """
    A view for editing a single vote
    """
    model = Vote
    form_class = VoteForm
    template_name = 'votes/update.pug'
    permission_required = 'votes.change_vote'


class VoteDeleteView(BaseDeleteView):
    """
    A view for deleting a single vote
    """
    model = Vote
    permission_required = 'votes.delete_vote'
    template_name = 'votes/delete.pug'
