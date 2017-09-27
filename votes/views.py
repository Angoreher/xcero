# -*- coding: utf-8 -*-
""" Views for the votes application. """
# standard library

# django

# models
from .models import Vote

# views
from base.views import BaseCreateView
from base.views import BaseDeleteView
from base.views import BaseDetailView
from base.views import BaseListView
from base.views import BaseUpdateView

# forms
from .forms import VoteForm


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


class VoteDetailView(BaseDetailView):
    """
    A view for displaying a single vote
    """
    model = Vote
    template_name = 'votes/detail.pug'
    permission_required = 'votes.view_vote'


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
