from django.contrib import admin

from .models import Flat
from .models import Complaint
from .models import Owner


class PropertyOwnerFlatsInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('owner', 'flat',)


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'id')
    readonly_fields = ["construction_year", ]
    list_display = (
        'address',
        'price',
        'new_building',
        'construction_year',
        'town')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)
    raw_id_fields = ('liked_by',)
    inlines = (PropertyOwnerFlatsInline,)


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat',)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'phonenumber',
        'normalized_phonenumber',)
    raw_id_fields = ('flats',)
