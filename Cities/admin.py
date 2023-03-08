from django.contrib import admin
from .models import City, Continent, Country

import adminactions.actions as actions

admin.site.register(Continent)
admin.site.register(Country)

class AdminCity(admin.ModelAdmin):
    list_display = ('country', 'label')
    list_filter = ('country',)

admin.site.register(City, AdminCity)
actions.add_to_site(admin.site)



