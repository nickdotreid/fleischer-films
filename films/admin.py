from django.contrib import admin

from films.models import Film, Tag, LinkType, Link
# Register your models here.

class LinkInline(admin.TabularInline):
    model = Link

class FilmAdmin(admin.ModelAdmin):
    date_hierarchy = 'release_date'

    fieldsets = (
        (None, {
            'fields': ('title', ('year', 'release_date'), 'duration')
        }),
        ("Notes", {
            'fields': ('description',)
        }),
    )

    inlines = [
    	LinkInline,
    ]

admin.site.register(Film, FilmAdmin)