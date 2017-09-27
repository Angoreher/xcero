# django
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# models
from base.models import BaseModel

# utils
from magic.utils import MagicClient


class CardSet(BaseModel):
    code = models.CharField(
        _('code'),
        max_length=255,
        null=True,
        blank=True,
    )
    name = models.CharField(
        _('name'),
        max_length=255,
        null=True,
        blank=True,
    )
    gatherer_code = models.CharField(
        _('gatherer code'),
        max_length=255,
        null=True,
        blank=True,
    )
    old_code = models.CharField(
        _('old_code'),
        max_length=255,
        null=True,
        blank=True,
    )
    magic_cards_info_code = models.CharField(
        _('magic cards info code'),
        max_length=255,
        null=True,
        blank=True,
    )
    release_date = models.CharField(
        _('release date'),
        max_length=255,
        null=True,
        blank=True,
    )
    border = models.CharField(
        _('barder'),
        max_length=255,
        null=True,
        blank=True,
    )
    set_type = models.CharField(
        _('type'),
        max_length=255,
        null=True,
        blank=True,
    )
    block = models.CharField(
        _('block'),
        max_length=255,
        null=True,
        blank=True,
    )
    online_only = models.CharField(
        _('online only'),
        max_length=255,
        null=True,
        blank=True,
    )
    booster = models.CharField(
        _('booster'),
        max_length=255,
        null=True,
        blank=True,
    )
    mkm_id = models.CharField(
        _('mkm_id'),
        max_length=255,
        null=True,
        blank=True,
    )
    mkm_name = models.CharField(
        _('mkm_name'),
        max_length=255,
        null=True,
        blank=True,
    )
    last_updated_at = models.DateTimeField(
        _('last updated at'),
        default=timezone.now,
        null=True,
        blank=True,
    )

    def __str__(self):
        return "{}, {}".format(self.name, self.code)

    @classmethod
    def update_sets_data(cls):
        magic_client = MagicClient()
        card_sets = magic_client.get_sets()

        for card_set in card_sets:
            _set, created = cls.objects.get_or_create(
                name=card_set.name,
            )

            for attr, value in card_set.__dict__.items():
                _set.attr = value

            if not created:
                _set.last_updated_at = timezone.now()

            _set.save()


class Card(BaseModel):
    card_set = models.ForeignKey(
        CardSet,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='cards',
        verbose_name=_('set'),
    )
    name = models.CharField(
        _('name'),
        max_length=255,
        null=True,
        blank=True,
    )
    multiverse_id = models.CharField(
        _('multiverse id'),
        max_length=255,
        null=True,
        blank=True,
    )
    layout = models.CharField(
        _('layout'),
        max_length=255,
        null=True,
        blank=True,
    )
    names = models.CharField(
        _('names'),
        max_length=255,
        null=True,
        blank=True,
    )
    mana_cost = models.CharField(
        _('mana cost'),
        max_length=255,
        null=True,
        blank=True,
    )
    cmc = models.CharField(
        _('converted mana cost'),
        max_length=255,
        null=True,
        blank=True,
    )
    colors = models.CharField(
        _('colors'),
        max_length=255,
        null=True,
        blank=True,
    )
    color_identity = models.CharField(
        _('color identity'),
        max_length=255,
        null=True,
        blank=True,
    )
    card_type = models.CharField(
        _('type'),
        max_length=255,
        null=True,
        blank=True,
    )
    card_supertypes = models.CharField(
        _('supertypes'),
        max_length=255,
        null=True,
        blank=True,
    )
    card_subtypes = models.CharField(
        _('subtypes'),
        max_length=255,
        null=True,
        blank=True,
    )
    rarity = models.CharField(
        _('rarity'),
        max_length=255,
        null=True,
        blank=True,
    )
    text = models.CharField(
        _('text'),
        max_length=255,
        null=True,
        blank=True,
    )
    flavor = models.CharField(
        _('flavor'),
        max_length=255,
        null=True,
        blank=True,
    )
    artist = models.CharField(
        _('artist'),
        max_length=255,
        null=True,
        blank=True,
    )
    number = models.CharField(
        _('number'),
        max_length=255,
        null=True,
        blank=True,
    )
    power = models.CharField(
        _('power'),
        max_length=255,
        null=True,
        blank=True,
    )
    toughness = models.CharField(
        _('toughness'),
        max_length=255,
        null=True,
        blank=True,
    )
    loyalty = models.CharField(
        _('loyalty'),
        max_length=255,
        null=True,
        blank=True,
    )
    variations = models.CharField(
        _('variations'),
        max_length=255,
        null=True,
        blank=True,
    )
    watermark = models.CharField(
        _('watermark'),
        max_length=255,
        null=True,
        blank=True,
    )
    border = models.CharField(
        _('border'),
        max_length=255,
        null=True,
        blank=True,
    )
    timeshifted = models.CharField(
        _('timeshifted'),
        max_length=255,
        null=True,
        blank=True,
    )
    hand = models.CharField(
        _('hand'),
        max_length=255,
        null=True,
        blank=True,
    )
    life = models.CharField(
        _('life'),
        max_length=255,
        null=True,
        blank=True,
    )
    reserved = models.CharField(
        _('reserved'),
        max_length=255,
        null=True,
        blank=True,
    )
    release_date = models.CharField(
        _('release date'),
        max_length=255,
        null=True,
        blank=True,
    )
    starter = models.CharField(
        _('starter'),
        max_length=255,
        null=True,
        blank=True,
    )
    rulings = models.CharField(
        _('rulings'),
        max_length=255,
        null=True,
        blank=True,
    )
    foreign_names = models.CharField(
        _('foreign_names'),
        max_length=255,
        null=True,
        blank=True,
    )
    printings = models.CharField(
        _('printings'),
        max_length=255,
        null=True,
        blank=True,
    )
    original_text = models.CharField(
        _('original text'),
        max_length=255,
        null=True,
        blank=True,
    )
    original_type = models.CharField(
        _('original type'),
        max_length=255,
        null=True,
        blank=True,
    )
    legalities = models.CharField(
        _('legalities'),
        max_length=255,
        null=True,
        blank=True,
    )
    source = models.CharField(
        _('source'),
        max_length=255,
        null=True,
        blank=True,
    )
    image_url = models.CharField(
        _('image url'),
        max_length=255,
        null=True,
        blank=True,
    )
    set_code = models.CharField(
        _('set_code'),
        max_length=255,
        null=True,
        blank=True,
    )
    set_name = models.CharField(
        _('set name'),
        max_length=255,
        null=True,
        blank=True,
    )
    external_id = models.CharField(
        _('external id'),
        max_length=255,
        null=True,
        blank=True,
    )
    last_updated_at = models.DateTimeField(
        _('last updated at'),
        default=timezone.now,
        max_length=255,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    @classmethod
    def update_cards_data(cls):
        magic_client = MagicClient()
        cards = magic_client.get_cards()

        for card in cards:
            _card, created = cls.objects.get_or_create(
                name=card.name,
            )

            for attr, value in card.__dict__.items():
                _card.attr = value

            try:
                _set = CardSet.objects.get(code=card.set)
                _card.card_set = _set
            except CardSet.DoesNotExist:
                raise

            if not created:
                _card.last_updated_at = timezone.now()

            _card.save()
