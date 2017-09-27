# -*- coding: utf-8 -*-
""" Administration classes for the votes application. """
# standard library

# django
from django.contrib import admin

# models
from .models import Vote


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    pass
