# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Page'
        db.create_table(u'pages_page', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nav_side', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('nav_pos', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('nav_show', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('nav_icon', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('nav_heading', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('page_heading', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('page_body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'pages', ['Page'])


    def backwards(self, orm):
        # Deleting model 'Page'
        db.delete_table(u'pages_page')


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
            'page_heading': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['pages']