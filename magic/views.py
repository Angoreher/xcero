# django
from django.core.urlresolvers import reverse

# models
from magic.models import Card
from magic.models import CardSet
from votes.models import Vote

# forms
from votes.forms import VoteForm

# views
from base.views import BaseListView
from base.views import BaseDetailView
from base.views import BaseRedirectView

# utils
from magic.utils import get_random_card


class CardSetListView(BaseListView):
    """
    View for displaying a list of set.
    """
    model = CardSet
    template_name = 'card_set/list.pug'


class CardSetDetailView(BaseDetailView):
    """
    A view for displaying a single card set
    """
    model = CardSet
    template_name = 'card_set/detail.pug'


class CardDetailView(BaseDetailView):
    """
    A view for displaying a single card
    """
    model = Card
    template_name = 'card/detail.pug'

    def get_context_data(self, **kwargs):
        context = super(CardDetailView, self).get_context_data(**kwargs)

        form_data = {
            'user': self.request.user,
            'card': self.get_object(),
        }

        context['form'] = VoteForm(form_data)

        return context


class CardSetVoteRedirectView(BaseRedirectView):

    def get_redirect_url(self, *args, **kwargs):
        card_set_id = kwargs.get('pk')
        unvoted_cards = Vote.get_not_voted_cards(
            self.request.user,
            card_set_id,
        )
        if not unvoted_cards:
            # TODO: add a message
            return reverse('card_set_list')

        card_id = get_random_card(unvoted_cards).pk

        return reverse('card_detail', args=[card_id])
