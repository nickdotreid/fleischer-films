# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Distributor'
        db.create_table(u'films_distributor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'films', ['Distributor'])

        # Adding field 'Film.current_distributor'
        db.add_column(u'films_film', 'current_distributor',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='current_films', null=True, to=orm['films.Distributor']),
                      keep_default=False)

        # Adding field 'Film.original_distributor'
        db.add_column(u'films_film', 'original_distributor',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='original_films', null=True, to=orm['films.Distributor']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Distributor'
        db.delete_table(u'films_distributor')

        # Deleting field 'Film.current_distributor'
        db.delete_column(u'films_film', 'current_distributor_id')

        # Deleting field 'Film.original_distributor'
        db.delete_column(u'films_film', 'original_distributor_id')


    models = {
        u'films.distributor': {
            'Meta': {'object_name': 'Distributor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'films.film': {
            'Meta': {'object_name': 'Film'},
            'copyright_claimant': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'copyright_status': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'copyright_status_source': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'current_distributor': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'current_films'", 'null': 'True', 'to': u"orm['films.Distributor']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '5000', 'null': 'True', 'blank': 'True'}),
            'duration': ('durationfield.db.models.fields.duration.DurationField', [], {'null': 'True', 'blank': 'True'}),
            'have_it': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'original_distributor': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'original_films'", 'null': 'True', 'to': u"orm['films.Distributor']"}),
            'release_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'series': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['films.Series']", 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'films'", 'blank': 'True', 'to': u"orm['films.Tag']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'work_notes': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'})
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
            'Meta': {'object_name': 'LinkType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'films.series': {
            'Meta': {'object_name': 'Series'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'films.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['films']