from django.contrib import admin

# Register your models here.
from listings.models import Band, Listing

# admin.site.register(Band)
class BandAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'year_formed', 'genre') # liste les champs que nous voulons sur l'affichage de la liste


class ListingAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'description', 'band')  # ajouter ‘band' ici


admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)
