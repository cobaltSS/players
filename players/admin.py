from django.contrib import admin
from players.models import Players
# Register your models here.
class PlayesrAdmin(admin.ModelAdmin):
    list_display = ['name', 'wins', 'lesions']

admin.site.register(Players, PlayesrAdmin)