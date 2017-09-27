# -*- coding: utf-8 -*-
""" Models for the votes application. """
# standard library

# django
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

# models
from base.models import BaseModel
from users.models import User


class Vote(BaseModel):
    # foreign keys
    user = models.ForeignKey(
        User,
        verbose_name=_('user'),
    )
    # required fields
    name = models.CharField(
        _('name'),
        max_length=30,
        blank=True,
    )
    # optional fields

    class Meta:
        verbose_name = _('vote')
        verbose_name_plural = _('votes')
        permissions = (
            ('view_vote', _('Can view votes')),
        )

    def __str__(self):
        # TODO this is an example str return, change it
        return self.name

    def get_absolute_url(self):
        """ Returns the canonical URL for the vote object """
        # TODO this is an example, change it
        return reverse('vote_detail', args=(self.pk,))
