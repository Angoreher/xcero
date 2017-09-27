# -*- coding: utf-8 -*-
""" Models for the stats application. """
# standard library

# django
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

# models
from base.models import BaseModel
from users.models import User


class Stat(BaseModel):
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
        verbose_name = _('stat')
        verbose_name_plural = _('stats')
        permissions = (
            ('view_stat', _('Can view stats')),
        )

    def __str__(self):
        # TODO this is an example str return, change it
        return self.name

    def get_absolute_url(self):
        """ Returns the canonical URL for the stat object """
        # TODO this is an example, change it
        return reverse('stat_detail', args=(self.pk,))
