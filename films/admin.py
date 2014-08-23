from django.contrib import admin
from django import forms

from suit.widgets import SuitDateWidget
from suit_redactor.widgets import RedactorWidget

from films.models import Film, Tag, LinkType, Link, Series, Distributor, ProductionCompany, FilmLocation, LocationType, Role, Person, Crew

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

class CrewInline(admin.TabularInline):
    model = Crew

class FilmAdmin(admin.ModelAdmin):
    date_hierarchy = 'release_date'
    filter_horizontal = ('tags',)

    search_fields = ('title', 'description', 'work_notes', 'series__name','tags__name', 'production_company__name', 'current_distributor__name', 'original_distributor__name')

    list_display = ('title','series','year', 'release_date')
    list_filter = ('tags','year', 'series')

    form = FilmAdminForm

    fieldsets = (
        (None, {
            'fields': (
            	'title',
            	'series',
            	'production_company',
            	('year', 'release_date'),
            	'duration',
                'description',
                'crew_notes',
            	)
        }),
        ("Notes", {
            'fields': (
            	('original_distributor', 'current_distributor'),
            	'work_notes',
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
        CrewInline,
        FilmLocation,
    	LinkInline,
    ]

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(FilmAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name in ['description', 'work_notes']:
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield

admin.site.register(Film, FilmAdmin)

class FilmInline(admin.TabularInline):
    model = Film
    fields = ('title','series','year')
    extra = 0

def merge_models(modeladmin, request, queryset, film_property):
    if not film_property:
        modeladmin.message_user(request, "Merge Property NOT Configured")
        return False

    count = 0
    models_list = list(queryset.all())
    modelMergedTo = models_list.pop()
    for m in models_list:    
        count += Film.objects.extra(where=[film_property+"_id=%s"], params=[m.id]).update(**{
            film_property:modelMergedTo,
            })
    modeladmin.message_user(request, "Merged %d films" % (count))
    return modelMergedTo



class AdminForInlineFilm(admin.ModelAdmin):
    inlines = [
        FilmInline,
    ]
    actions = [
        'merge_models'
    ]
    film_property = False
    def merge_models(self, request, queryset):
        modelMergedTo = merge_models(self, request, queryset, self.film_property)
        queryset.exclude(id=modelMergedTo.id).delete()
    merge_models.short_description = "Merge selected models"

class SeriesAdmin(AdminForInlineFilm):
    film_property = 'series'
    merge_models.short_description = "Merge selected Series"

class ProductionCompanyAdmin(AdminForInlineFilm):
    film_property = 'production_company'
    merge_models.short_description = "Merge selected Production Company"

class DistributorAdmin(admin.ModelAdmin):
    actions = [
        'merge_models'
    ]
    def merge_models(self,request,queryset):
        modelMergedTo = merge_models(self, request, queryset, 'current_distributor')
        modelMergedTo = merge_models(self, request, queryset, 'original_distributor')
        queryset.exclude(id=modelMergedTo.id).delete()
    merge_models.short_description = "Merge selected models"


admin.site.register(Series,SeriesAdmin)
admin.site.register(ProductionCompany,ProductionCompanyAdmin)
admin.site.register(Distributor,DistributorAdmin)
admin.site.register(LinkType)
admin.site.register(LocationType)
admin.site.register(Person)
admin.site.register(Role)
admin.site.register(Tag)