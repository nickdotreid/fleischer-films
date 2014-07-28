from django.db import models
from datetime import datetime

from durationfield.db.models.fields.duration import DurationField

YEARS = []
for y in range(1915, (datetime.now().year + 1)):
	YEARS.append((y,y))

class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class ProductionCompany(models.Model):
    class Meta:
        verbose_name = 'Production Company'
        verbose_name_plural = 'Production Companys'

    name = models.CharField(max_length=150)

    def __unicode__(self):
        return self.name
    

class Distributor(models.Model):
    class Meta:
        verbose_name = 'Distributor'
        verbose_name_plural = 'Distributors'

    name = models.CharField(max_length=150)

    def __unicode__(self):
        return self.name
    

class Series(models.Model):
    class Meta:
        verbose_name = 'Series'
        verbose_name_plural = 'Series'

    name = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name
    

class Film(models.Model):
    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Films'

    title = models.CharField(null=False, blank=False, max_length=250)
    release_date = models.DateField(null=True, blank=True)
    year = models.IntegerField(choices=YEARS, max_length=4, null=True, blank=True)
    series = models.ForeignKey(Series, null=True, blank=True)

    production_company = models.ForeignKey(ProductionCompany, null=True, blank=True)


    current_distributor = models.ForeignKey(Distributor, related_name="current_films", null=True, blank=True)
    original_distributor = models.ForeignKey(Distributor, related_name="original_films", null=True, blank=True)

    description = models.CharField(null=True, blank=True, max_length=5000)
    duration = DurationField(null=True, blank=True)

    tags = models.ManyToManyField(Tag, blank=True, related_name='films')

    have_it = models.BooleanField(default=False)
    work_notes = models.CharField(null=True, blank=True, max_length=5000)

    copyright_status = models.CharField(null=True, blank=True, max_length=250)
    copyright_status_source = models.CharField(null=True, blank=True, max_length=250)
    copyright_claimant = models.CharField(null=True, blank=True, max_length=250)

    def __unicode__(self):
    	if self.year:
    		return "%s (%d)" % (self.title, self.year)
        return self.title

class LinkType(models.Model):
    class Meta:
        verbose_name = 'LinkType'
        verbose_name_plural = 'LinkTypes'

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
    