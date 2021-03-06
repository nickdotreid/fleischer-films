from django.contrib import admin
from django import forms

from suit.widgets import SuitDateWidget
from suit_redactor.widgets import RedactorWidget

from films.models import Film, Tag, LinkType, Link, Series, Distributor, DistributorInformation, ProductionCompany, FilmLocation, LocationType, Role, Person, Crew, CopyrightStatus

from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin

class FilmResource(resources.ModelResource):    
    class Meta:
        model = Film
        fields = (
            'id','title','release_date','year','series', 'duration', 'tags',
            'description', 'work_notes',
            'production_company', 'original_distributor',
            'copyright_status', 'copyright_status_source', 'copyright_claimant',
            'crew_notes', 'crew',
            )

    crew = fields.Field(column_name='Cast and Crew')
    def dehydrate_crew(self, film):
        members = Crew.objects.filter(film=film).all()
        return '\n'.join(["%s, %s" % (c.person.name, c.role.name) for c in members])

    def dehydrate_tags(self, film):
        return ', '.join([t.name for t in film.tags.all()])

    def dehydrate_series(self,film):
        if film.series:
            return film.series.name
        return None
    def dehydrate_original_distributor(self, film):
        if film.original_distributor:
            return film.original_distributor.name
        return None
    def dehydrate_copyright_status(self,film):
        if film.copyright_status:
            return film.copyright_status.name
        return None
    def dehydrate_production_company(self, film):
        if film.production_company:
            return film.production_company.name
        return None


class DistributorInline(admin.TabularInline):
    model = DistributorInformation


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
    verbose_name_plural = "Cast and Crew"
    model = Crew


class FilmLocationFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'Film Location'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'decade'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('True', "Have it"),
            ('False', "Don't have it"),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == 'True':
            return queryset.exclude(locations=None)
        if self.value() == 'False':
            return queryset.filter(locations=None)

class FilmAdmin(ImportExportModelAdmin):
    resource_class = FilmResource

    date_hierarchy = 'release_date'
    filter_horizontal = ('tags',)

    search_fields = ('title', 'description', 'work_notes',
        'series__name','tags__name', 'production_company__name',
        'original_distributor__name', 'distributors__distributor__name',
        'copyright_status__name', 'copyright_claimant',
        'crew__person__name',
        )

    list_display = ('title','series','year', 'release_date')
    list_filter = ('tags','year', 'series', FilmLocationFilter)

    form = FilmAdminForm

    fieldsets = (
        (None, {
            'fields': (
            	'title',
            	'series',
            	'production_company',
            	('year', 'release_date'),
                'image',
            	'duration',
                'description',
                'crew_notes',
            	)
        }),
        ("Notes", {
            'fields': (
            	'original_distributor',
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
        DistributorInline,
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

class PeopleAdmin(admin.ModelAdmin):

    search_fields = ('name',)

    inlines = [
        CrewInline,
    ]

admin.site.register(Person, PeopleAdmin)

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
    search_fields = ('name',)

admin.site.register(Series,SeriesAdmin)
admin.site.register(ProductionCompany,ProductionCompanyAdmin)
admin.site.register(Distributor,DistributorAdmin)
admin.site.register(LinkType)
admin.site.register(LocationType)
admin.site.register(Role)

class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)
admin.site.register(Tag, TagAdmin)
admin.site.register(CopyrightStatus)