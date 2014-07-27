# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LinkType'
        db.create_table(u'films_linktype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'films', ['LinkType'])

        # Adding model 'Link'
        db.create_table(u'films_link', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('film', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['films.Film'])),
            ('link_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['films.LinkType'])),
            ('href', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'films', ['Link'])


    def backwards(self, orm):
        # Deleting model 'LinkType'
        db.delete_table(u'films_linktype')

        # Deleting model 'Link'
        db.delete_table(u'films_link')


    models = {
        u'films.film': {
            'Meta': {'object_name': 'Film'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '5000', 'null': 'True', 'blank': 'True'}),
            'duration': ('durationfield.db.models.fields.duration.DurationField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'release_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'year': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'})
        },
        u'films.link': {
            'Meta': {'object_name': 'Link'},
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
        u'films.tag': {
            'Meta': {'object_name': 'Tag'},
            'films': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'tags'", 'symmetrical': 'False', 'to': u"orm['films.Film']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['films']