from django.contrib import admin
from django import forms

from films.models import Film, Tag, LinkType, Link, Series
# Register your models here.

class LinkInline(admin.TabularInline):
    model = Link

class FilmAdmin(admin.ModelAdmin):
    date_hierarchy = 'release_date'
    filter_horizontal = ('tags',)

    fieldsets = (
        (None, {
            'fields': (
            	'title',
            	'series',
            	('year', 'release_date'),
            	'duration',
            	)
        }),
        ("Notes", {
            'fields': (
            	'have_it',
            	'work_notes',
            	'description',
            	'tags',
            	)
        }),
    )

    inlines = [
    	LinkInline,
    ]

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(FilmAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name in ['description', 'work_notes']:
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield

admin.site.register(Film, FilmAdmin)
admin.site.register(Series)
admin.site.register(LinkType)
admin.site.register(Tag)