# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Film'
        db.create_table(u'films_film', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('release_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=5000, null=True)),
            ('duration', self.gf('durationfield.db.models.fields.duration.DurationField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'films', ['Film'])


    def backwards(self, orm):
        # Deleting model 'Film'
        db.delete_table(u'films_film')


    models = {
        u'films.film': {
            'Meta': {'object_name': 'Film'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '5000', 'null': 'True'}),
            'duration': ('durationfield.db.models.fields.duration.DurationField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'release_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'year': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['films']