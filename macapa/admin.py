from django.contrib import admin

from .models import MacapaContact


class MacapaContactAdmin(admin.ModelAdmin):
    list_display = ('nome', 'celular')
    list_filter = list_display
    search_fields = list_display
    fields = list_display


admin.site.register(MacapaContact, MacapaContactAdmin)
