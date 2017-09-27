# -*- coding: utf-8 -*-
""" Views for the stats application. """
# standard library

# django

# models
from .models import Stat

# views
from base.views import BaseCreateView
from base.views import BaseDeleteView
from base.views import BaseDetailView
from base.views import BaseListView
from base.views import BaseUpdateView

# forms
from .forms import StatForm


class StatListView(BaseListView):
    """
    View for displaying a list of stats.
    """
    model = Stat
    template_name = 'stats/list.pug'
    permission_required = 'stats.view_stat'


class StatCreateView(BaseCreateView):
    """
    A view for creating a single stat
    """
    model = Stat
    form_class = StatForm
    template_name = 'stats/create.pug'
    permission_required = 'stats.add_stat'


class StatDetailView(BaseDetailView):
    """
    A view for displaying a single stat
    """
    model = Stat
    template_name = 'stats/detail.pug'
    permission_required = 'stats.view_stat'


class StatUpdateView(BaseUpdateView):
    """
    A view for editing a single stat
    """
    model = Stat
    form_class = StatForm
    template_name = 'stats/update.pug'
    permission_required = 'stats.change_stat'


class StatDeleteView(BaseDeleteView):
    """
    A view for deleting a single stat
    """
    model = Stat
    permission_required = 'stats.delete_stat'
    template_name = 'stats/delete.pug'
