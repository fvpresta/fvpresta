# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Client.url'
        db.add_column('cms_client', 'url',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'Client.display_order'
        db.add_column('cms_client', 'display_order',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Client.url'
        db.delete_column('cms_client', 'url')

        # Deleting field 'Client.display_order'
        db.delete_column('cms_client', 'display_order')


    models = {
        'cms.capture': {
            'Meta': {'object_name': 'Capture'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'captures'", 'to': "orm['cms.Project']"})
        },
        'cms.carousel': {
            'Meta': {'object_name': 'Carousel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'cms.client': {
            'Meta': {'ordering': "['display_order']", 'object_name': 'Client'},
            'display_order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200'})
        },
        'cms.project': {
            'Meta': {'object_name': 'Project'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects'", 'to': "orm['cms.Client']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['cms']