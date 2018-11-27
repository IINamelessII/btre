from django.contrib import admin
from realtors.models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('name',)
    list_per_page = 25
    search_fields = ('name',)


admin.site.register(Realtor, RealtorAdmin)
