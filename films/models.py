from django.db import models
from datetime import datetime

from sorl.thumbnail import ImageField
from durationfield.db.models.fields.duration import DurationField

YEARS = []
for y in range(1915, (datetime.now().year + 1)):
	YEARS.append((y,y))

class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['name']

    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class ProductionCompany(models.Model):
    class Meta:
        verbose_name = 'Production Company'
        verbose_name_plural = 'Production Companies'
        ordering = ['name']

    name = models.CharField(max_length=150)

    def __unicode__(self):
        return self.name
    

class Distributor(models.Model):
    class Meta:
        verbose_name = 'Distributor'
        verbose_name_plural = 'Distributors'
        ordering = ['name']

    name = models.CharField(max_length=150)

    def __unicode__(self):
        return self.name
    

class Series(models.Model):
    class Meta:
        verbose_name = 'Series'
        verbose_name_plural = 'Series'
        ordering = ['name']

    name = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name

class CopyrightStatus(models.Model):
    class Meta:
        ordering = ['name']
    name = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name
    

class Film(models.Model):
    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Films'
        ordering = ['title']

    title = models.CharField(null=False, blank=False, max_length=250)
    release_date = models.DateField(null=True, blank=True)
    year = models.IntegerField(choices=YEARS, max_length=4, null=True, blank=True)
    series = models.ForeignKey(Series, null=True, blank=True)

    image = ImageField(verbose_name=u'Featured Image', upload_to="film_images" ,null=True, blank=True)

    production_company = models.ForeignKey(ProductionCompany, null=True, blank=True)

    current_distributor = models.ForeignKey(Distributor, verbose_name='Additional distributor', related_name="current_films", null=True, blank=True)
    original_distributor = models.ForeignKey(Distributor, related_name="original_films", null=True, blank=True)

    description = models.CharField(null=True, blank=True, max_length=5000)
    duration = DurationField(verbose_name="runtime",null=True, blank=True)

    tags = models.ManyToManyField(Tag, blank=True, related_name='films')

    work_notes = models.CharField(null=True, blank=True, max_length=5000)
    crew_notes = models.TextField(verbose_name="Notes", null=True, blank=True)

    copyright_status = models.ForeignKey(CopyrightStatus, null=True, blank=True)
    copyright_status_source = models.CharField(null=True, blank=True, max_length=250)
    copyright_claimant = models.TextField(verbose_name="Copyright details", null=True, blank=True)

    def __unicode__(self):
    	if self.year:
    		return "%s (%d)" % (self.title, self.year)
        return self.title

class LinkType(models.Model):
    class Meta:
        verbose_name = 'Link Type'
        verbose_name_plural = 'Link Types'
        ordering = ['name']

    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name
    

class Link(models.Model):
    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'

    film = models.ForeignKey(Film)
    link_type = models.ForeignKey(LinkType)
    href = models.CharField(max_length=250)
    description = models.CharField(null=True, blank=True, max_length=500)

    def __unicode__(self):
        return "%s, (%s)" % (self.film.title, self.link_type.name)

class LocationType(models.Model):
    class Meta:
        ordering = ['name']
    name = models.CharField(max_length=150)

    def __unicode__(self):
        return self.name

class FilmLocation(models.Model):
    film = models.ForeignKey(Film, related_name='locations')
    source_type = models.ForeignKey(LocationType, verbose_name="Source", blank=True, null=True)
    source = models.CharField(max_length=200, verbose_name="Location", blank=True, null=True)
    notes = models.CharField(max_length=2500, blank=True, null=True)
    have_it = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s, %s (%s)" % (self.film.title, self.source, self.source_type.name)

class Person(models.Model):
    class Meta:
        ordering = ['name']
    name = models.CharField(max_length=150)
    notes = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

class Role(models.Model):
    class Meta:
        ordering = ['name']
    name = models.CharField(max_length=150)

    def __unicode__(self):
        return self.name

class Crew(models.Model):
    film = models.ForeignKey(Film)
    person = models.ForeignKey(Person)
    role = models.ForeignKey(Role)
    notes = models.CharField(blank=True, null=True, max_length=50)

    def __unicode__(self):
        return "%s: %s (%s)" % (self.film.title, self.person.name, self.role.name)