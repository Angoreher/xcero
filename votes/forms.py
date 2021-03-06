# -*- coding: utf-8 -*-
""" Forms for the votes application. """
# standard library


# django
from django import forms

# models
from .models import Vote

# views
from base.forms import BaseModelForm


class VoteForm(BaseModelForm):
    """
    Form Vote model.
    """
    score = forms.IntegerField(required=True)

    class Meta:
        model = Vote
        widgets = {
            'user': forms.HiddenInput(),
            'card': forms.HiddenInput(),
        }
        exclude = ()
