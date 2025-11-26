from django.contrib import admin
from viewer.models import *
from logging import getLogger

from django.urls import reverse_lazy
from django.views.generic import FormView, ListView

from viewer.models import Item

admin.site.register(Item)
admin.site.register(Brand)
admin.site.register(Type)
admin.site.register(Review)

LOGGER = getLogger()
