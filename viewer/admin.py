from django.contrib import admin
from viewer.models import *
from logging import getLogger

from django.urls import reverse_lazy
from django.views.generic import FormView, ListView

from viewer.models import Item, ItemImage

admin.site.register(Brand)
admin.site.register(Type)
admin.site.register(Review)

LOGGER = getLogger()

class ItemImageInline(admin.TabularInline):
    model = ItemImage
    extra = 3

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemImageInline]