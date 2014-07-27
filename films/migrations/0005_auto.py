# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field films on 'Tag'
        db.delete_table(db.shorten_name(u'films_tag_films'))

        # Adding M2M table for field tags on 'Film'
        m2m_table_name = db.shorten_name(u'films_film_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('film', models.ForeignKey(orm[u'films.film'], null=False)),
            ('tag', models.ForeignKey(orm[u'films.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['film_id', 'tag_id'])


    def backwards(self, orm):
        # Adding M2M table for field films on 'Tag'
        m2m_table_name = db.shorten_name(u'films_tag_films')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tag', models.ForeignKey(orm[u'films.tag'], null=False)),
            ('film', models.ForeignKey(orm[u'films.film'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tag_id', 'film_id'])

        # Removing M2M table for field tags on 'Film'
        db.delete_table(db.shorten_name(u'films_film_tags'))


    models = {
        u'films.film': {
            'Meta': {'object_name': 'Film'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '5000', 'null': 'True', 'blank': 'True'}),
            'duration': ('durationfield.db.models.fields.duration.DurationField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'release_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'films'", 'blank': 'True', 'to': u"orm['films.Tag']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
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
        u'films.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['films']