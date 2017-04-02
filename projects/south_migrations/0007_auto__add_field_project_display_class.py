# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Project.display_class'
        db.add_column(u'projects_project', 'display_class',
                      self.gf('django.db.models.fields.CharField')(default='bh_dots', max_length=32),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Project.display_class'
        db.delete_column(u'projects_project', 'display_class')


    models = {
        u'projects.entry': {
            'Meta': {'ordering': "['-posted']", 'object_name': 'Entry'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projectentry'", 'to': u"orm['projects.Project']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'projects.externalprojectlink': {
            'Meta': {'object_name': 'ExternalProjectLink'},
            'icon': ('django.db.models.fields.CharField', [], {'default': "'fa-external-link'", 'max_length': '32', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'links'", 'to': u"orm['projects.Project']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '256'})
        },
        u'projects.inlineentryimg': {
            'Meta': {'ordering': "['-title']", 'object_name': 'InlineEntryImg'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('uuidfield.fields.UUIDField', [], {'unique': 'True', 'max_length': '32', 'blank': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'projects.project': {
            'Meta': {'object_name': 'Project'},
            'blurb': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'display_class': ('django.db.models.fields.CharField', [], {'default': "'bh_dots'", 'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['projects']