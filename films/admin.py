from django.contrib import admin
from django import forms

from suit.widgets import SuitDateWidget
from suit_redactor.widgets import RedactorWidget

from films.models import Film, Tag, LinkType, Link, Series, Distributor, ProductionCompany, FilmLocation

class FilmLocation(admin.TabularInline):
    model = FilmLocation

class LinkInline(admin.TabularInline):
    model = Link

class FilmAdminForm(forms.ModelForm):
    class Meta:
        widgets = {
            'description': RedactorWidget(editor_options={'lang': 'en'}),
            'release_date':SuitDateWidget,
        }

class FilmAdmin(admin.ModelAdmin):
    date_hierarchy = 'release_date'
    filter_horizontal = ('tags',)

    search_fields = ('title', 'description', 'work_notes', 'series','tags', 'production_company')

    list_display = ('title','series','year')
    list_filter = ('tags','year','series','production_company')

    form = FilmAdminForm

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
            	('original_distributor', 'current_distributor'),
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
        FilmLocation,
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