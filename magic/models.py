# standard library
from datetime import datetime

# django
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

# models
from base.models import BaseModel

# utils
from magic.utils import MagicClient
from magic.utils import MagicMapper


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
    release_date = models.DateTimeField(
        _('release date'),
        null=True,
        blank=True,
    )
    border = models.CharField(
        _('border'),
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
    booster = JSONField(
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

    class Meta:
        ordering = ['-release_date']

    def __str__(self):
        return "{}, {}".format(self.name, self.code)

    @classmethod
    def update_sets_data(cls, card_sets):
        if hasattr(card_sets, "__iter__"):
            for card_set in card_sets:
                cls.update_set_from_external_object(card_set)
        else:
            card_set = card_sets
            cls.update_set_from_external_object(card_set)

    @classmethod
    def update_set_from_external_object(cls, card_set):
            _set, created = cls.objects.get_or_create(
                name=card_set.name,
            )

            attr_map_dict = MagicMapper.SET_TO_MODEL

            for attr, value in card_set.__dict__.items():
                if attr in attr_map_dict:
                    attr = attr_map_dict[attr]

                if attr == 'release_date':
                    value = datetime.strptime(value, '%Y-%m-%d')

                setattr(_set, attr, value)

            if not created:
                _set.last_updated_at = timezone.now()

            try:
                _set.save()
            except Exception as e:
                print(_set.__dict__)
                print(e)

    @classmethod
    def update_set(cls, set_code):
        magic_client = MagicClient()
        card_sets = magic_client.get_set_by_set_code(set_code)
        cls.update_sets_data(card_sets)

    @classmethod
    def update_all_sets(cls):
        magic_client = MagicClient()
        card_sets = magic_client.get_sets()
        cls.update_sets_data(card_sets)

    def get_absolute_url(self):
        """ Returns the canonical URL for the card set object """
        return reverse('card_set_detail', args=(self.pk,))


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
    cmc = models.IntegerField(
        _('converted mana cost'),
        null=True,
        blank=True,
    )
    colors = models.ManyToManyField(
        'Color',
        related_name="card_colors",
        verbose_name=_('colors'),
    )
    color_identity = JSONField(
        null=True,
        blank=True,
    )
    card_type = models.CharField(
        _('card_type'),
        max_length=255,
        null=True,
        blank=True,
    )

    card_types = JSONField(
        null=True,
        blank=True,
    )
    card_supertypes = JSONField(
        null=True,
        blank=True,
    )
    card_subtypes = JSONField(
        null=True,
        blank=True,
    )
    rarity = models.CharField(
        _('rarity'),
        max_length=255,
        null=True,
        blank=True,
    )
    text = models.TextField(
        _('text'),
        null=True,
        blank=True,
    )
    flavor = models.TextField(
        _('flavor'),
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
    rulings = models.TextField(
        _('rulings'),
        null=True,
        blank=True,
    )
    foreign_names = JSONField(
        null=True,
        blank=True,
    )
    printings = JSONField(
        null=True,
        blank=True,
    )
    original_text = models.TextField(
        _('original text'),
        null=True,
        blank=True,
    )
    original_type = models.CharField(
        _('original type'),
        max_length=255,
        null=True,
        blank=True,
    )
    legalities = JSONField(
        _('legalities'),
        null=True,
        blank=True,
    )
    source = models.CharField(
        _('source'),
        max_length=255,
        null=True,
        blank=True,
    )
    image_url = models.URLField(
        _('image url'),
        max_length=1023,
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
    def update_card_data(cls, cards):
        attr_map_dict = MagicMapper.CARD_TO_MODEL
        for card in cards:
            _card, created = cls.objects.get_or_create(
                name=card.name,
            )

            for attr, value in card.__dict__.items():
                if attr in attr_map_dict:
                    attr = attr_map_dict[attr]

                _attr = getattr(_card, attr)

                if attr == 'colors':
                    cls.set_colors_relations(
                        _card, _attr, attr, value
                    )
                    continue

                if attr == 'card_set':
                    cls.set_card_set_relation(
                        _card, _attr, attr, value
                    )
                    continue

                setattr(_card, attr, value)

            if not created:
                _card.last_updated_at = timezone.now()

            _card.save()

    @classmethod
    def set_colors_relations(cls, _card, _attr, attr, value):
        if not value:
            return

        for color in value:
            _color, created = Color.objects.get_or_create(
                name=color,
            )
            if created:
                _color.letter = color[0].capitalize()
                _color.save()

            _card.colors.add(_color)

    @classmethod
    def set_card_set_relation(cls, _card, _attr, attr, value):
        try:
            card_set = CardSet.objects.get(
                code=value,
            )
            _card.card_set = card_set
            _card.save()
        except:
            CardSet.update_set(value)
            _set = CardSet.objects.get(code=value)
            _card.card_set = _set
            _card.save()

    @classmethod
    def update_all_cards(cls):
        magic_client = MagicClient()
        cards = magic_client.get_cards()
        cls.update_card_data(cards)

    @classmethod
    def update_cards_from_set(cls, set_code):
        magic_client = MagicClient()
        cards = magic_client.get_cards_by_set_code(set_code)
        cls.update_card_data(cards)

    def update_card(self):
        magic_client = MagicClient()
        cards = magic_client.get_card_by_name(self.name)
        self.update_card_data(cards)


class Archetype(BaseModel):
    name = models.CharField(
        _('name'),
        max_length=255,
    )
    colors = models.ManyToManyField(
        'Color',
        related_name='archetype_colors',
    )
    is_tribal = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.name


class Color(BaseModel):
    name = models.CharField(
        _('name'),
        max_length=255,
    )
    letter = models.CharField(
        _('letter'),
        max_length=1,
    )

    def __str__(self):
        return self.name
