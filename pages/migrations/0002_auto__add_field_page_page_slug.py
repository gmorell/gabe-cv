# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Page.page_slug'
        db.add_column(u'pages_page', 'page_slug',
                      self.gf('django.db.models.fields.SlugField')(default='', max_length=16),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Page.page_slug'
        db.delete_column(u'pages_page', 'page_slug')


    models = {
        u'pages.page': {
            'Meta': {'object_name': 'Page'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nav_heading': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'nav_icon': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'nav_pos': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'nav_show': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nav_side': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'page_body': ('django.db.models.fields.TextField', [], {}),
            'page_heading': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'page_slug': ('django.db.models.fields.SlugField', [], {'max_length': '16'})
        }
    }

    complete_apps = ['pages']