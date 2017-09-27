# -*- coding: utf-8 -*-
""" Forms for the stats application. """
# standard library

# django
from django import forms

# models
from .models import Stat

# views
from base.forms import BaseModelForm


class StatForm(BaseModelForm):
    """
    Form Stat model.
    """

    class Meta:
        model = Stat
        exclude = ()
