from django.contrib import admin

from films.models import Film
# Register your models here.

class FilmAdmin(admin.ModelAdmin):
    date_hierarchy = 'release_date'

    fieldsets = (
        (None, {
            'fields': ('title', 'year', 'release_date', 'duration')
        }),
        ("Notes", {
            'fields': ('description',)
        }),
    )

admin.site.register(Film, FilmAdmin)