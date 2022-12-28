from django.contrib import admin

from .models import Flat
from .models import Complaint
from .models import Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town',)
    readonly_fields = ["construction_year", ]
    list_display = (
        'address',
        'price',
        'owners_phonenumber',
        'normalized_owners_phonenumber',
        'new_building',
        'construction_year',
        'town')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)
    raw_id_fields = ('liked_by',)


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat',)


class OwnerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'phonenumber',
        'normalized_phonenumber',)
    raw_id_fields = ('flats',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
