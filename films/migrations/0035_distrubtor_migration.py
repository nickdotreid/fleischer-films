# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        for film in orm.Film.objects.all():
            for dist in [film.original_distributor, film.current_distributor]:
                if not dist:
                    continue
                di = orm.DistributorInformation(film=film, distributor=dist)
                di.save()

    def backwards(self, orm):
        raise RuntimeError("Cannot reverse this migration.")

    models = {
        u'films.copyrightstatus': {
            'Meta': {'ordering': "['name']", 'object_name': 'CopyrightStatus'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'films.crew': {
            'Meta': {'object_name': 'Crew'},
            'film': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'crew'", 'to': u"orm['films.Film']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'credits'", 'to': u"orm['films.Person']"}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['films.Role']"})
        },
        u'films.distributor': {
            'Meta': {'ordering': "['name']", 'object_name': 'Distributor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'films.distributorinformation': {
            'Meta': {'object_name': 'DistributorInformation'},
            'distributor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['films.Distributor']"}),
            'end_year': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'film': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['films.Film']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'original': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_year': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'})
        },
        u'films.film': {
            'Meta': {'ordering': "['title']", 'object_name': 'Film'},
            'copyright_claimant': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'copyright_status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['films.CopyrightStatus']", 'null': 'True', 'blank': 'True'}),
            'copyright_status_source': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'crew_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'current_distributor': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'current_films'", 'null': 'True', 'to': u"orm['films.Distributor']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '5000', 'null': 'True', 'blank': 'True'}),
            'distributors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['films.Distributor']", 'through': u"orm['films.DistributorInformation']", 'symmetrical': 'False'}),
            'duration': ('durationfield.db.models.fields.duration.DurationField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'original_distributor': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'original_films'", 'null': 'True', 'to': u"orm['films.Distributor']"}),
            'production_company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['films.ProductionCompany']", 'null': 'True', 'blank': 'True'}),
            'release_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'series': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['films.Series']", 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'films'", 'blank': 'True', 'to': u"orm['films.Tag']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'work_notes': ('django.db.models.fields.CharField', [], {'max_length': '5000', 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'})
        },
        u'films.filmlocation': {
            'Meta': {'object_name': 'FilmLocation'},
            'film': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'locations'", 'to': u"orm['films.Film']"}),
            'have_it': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '2500', 'null': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'source_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['films.LocationType']", 'null': 'True', 'blank': 'True'})
        },
        u'films.link': {
            'Meta': {'object_name': 'Link'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'film': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['films.Film']"}),
            'href': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['films.LinkType']"})
        },
        u'films.linktype': {
            'Meta': {'ordering': "['name']", 'object_name': 'LinkType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'films.locationtype': {
            'Meta': {'ordering': "['name']", 'object_name': 'LocationType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'films.person': {
            'Meta': {'ordering': "['name']", 'object_name': 'Person'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'films.productioncompany': {
            'Meta': {'ordering': "['name']", 'object_name': 'ProductionCompany'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'films.role': {
            'Meta': {'ordering': "['name']", 'object_name': 'Role'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'films.series': {
            'Meta': {'ordering': "['name']", 'object_name': 'Series'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'films.tag': {
            'Meta': {'ordering': "['name']", 'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['films']
    symmetrical = True
