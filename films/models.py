from django.db import models
from datetime import datetime

from durationfield.db.models.fields.duration import DurationField

YEARS = []
for y in range(1915, (datetime.now().year + 1)):
	YEARS.append((y,y))

class Film(models.Model):
    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Films'

    title = models.CharField(null=False, blank=False, max_length=250)
    release_date = models.DateField(null=True, blank=True)
    year = models.IntegerField(choices=YEARS, max_length=4, null=True, blank=True)

    description = models.CharField(null=True, blank=True, max_length=5000)
    duration = DurationField(null=True, blank=True)

    def __unicode__(self):
    	if self.year:
    		return "%s (%d)" % (self.title, self.year)
        return self.title
    
class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    films = models.ManyToManyField(Film, related_name='tags')
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

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

    def __unicode__(self):
        return "%s, (%s)" % (self.film.title, self.link_type.name)
    