from django.contrib import admin

from apps.examen.models import Examen


@admin.register(Examen)
class ExamenAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'profesor', 'descripcion', 'materia',)
    search_fields = ('titulo',)
    list_filter = ('titulo',)
