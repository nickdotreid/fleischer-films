from django.contrib import admin
from django import forms

from films.models import Film, Tag, LinkType, Link, Series, Distributor, ProductionCompany

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
            	'production_company',
            	('year', 'release_date'),
            	'duration',
            	)
        }),
        ("Notes", {
            'fields': (
            	'have_it',
            	('current_distributor','original_distributor'),
            	'work_notes',
            	'description',
            	'tags',
            	)
        }),
        ("Copyright",{
        	'classes':'collapsiable',
        	'fields':(
        		'copyright_status',
				'copyright_status_source',
				'copyright_claimant',
        		),
        	})
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
admin.site.register(ProductionCompany)
admin.site.register(Distributor)
admin.site.register(LinkType)
admin.site.register(Tag)