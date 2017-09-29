# -*- coding: utf-8 -*-
""" Models for the votes application. """
# standard library

# django
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.conf import settings

# models
from base.models import BaseModel
from users.models import User
from magic.models import Card
from magic.models import Archetype


class Vote(BaseModel):
    # foreign keys
    user = models.ForeignKey(
        User,
        verbose_name=_('user'),
    )
    card = models.ForeignKey(
        Card,
        related_name='cards',
        verbose_name=_('user'),
        on_delete=models.SET_NULL,
        null=True
    )

    # required fields

    # optional fields
    score = models.SmallIntegerField(
        _('score'),
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _('vote')
        verbose_name_plural = _('votes')
        permissions = (
            ('view_vote', _('Can view votes')),
        )

    def __str__(self):
        return "{}, {}, {}".format(
            self.user,
            self.card.name,
            self.standalone,
        )

    def get_absolute_url(self):
        """ Returns the canonical URL for the vote object """
        return reverse('vote_detail', args=(self.pk,))


class ArchetypeVote(BaseModel):
    # foreign keys
    vote = models.ForeignKey(
        'Vote',
        related_name='archetype_votes',
        verbose_name='archetype vote',
    )
    archetype = models.ForeignKey(
        Archetype,
        related_name="votes",
        verbose_name=_("archetype votes"),
    )
    score = models.SmallIntegerField(
        _('score'),
        validators=[
            MinValueValidator(settings.MIN_VOTE_VALUE),
            MaxValueValidator(settings.MAX_VOTE_VALUE),
        ]
    )

    def __str__(self):
        return "{}, {}, {}".format(
            self.vote,
            self.archetype.name,
            self.score,
        )
