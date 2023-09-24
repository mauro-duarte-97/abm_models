from django.contrib import admin

from apps.materia.models import Materia


@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'profesor',)
    search_fields = ('nombre',)
    list_filter = ('nombre',)
