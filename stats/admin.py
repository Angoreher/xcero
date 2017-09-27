# -*- coding: utf-8 -*-
""" Administration classes for the stats application. """
# standard library

# django
from django.contrib import admin

# models
from .models import Stat


@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    pass
