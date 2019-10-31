from django.contrib import admin
from .models import Past

class PastAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'past_job')

admin.site.register(Past, PastAdmin)