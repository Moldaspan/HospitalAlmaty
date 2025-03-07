from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Hospital, PopulationGrid, CityDistrict

@admin.register(Hospital)
class HospitalAdmin(OSMGeoAdmin):
    list_display = ("name", "address", "district", "location")

@admin.register(PopulationGrid)
class PopulationGridAdmin(admin.ModelAdmin):
    list_display = ("region_name", "total_population")

@admin.register(CityDistrict)
class CityDistrictAdmin(OSMGeoAdmin):
    list_display = ("name_ru", "geometry")
