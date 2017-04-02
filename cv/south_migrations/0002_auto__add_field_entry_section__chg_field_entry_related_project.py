# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Entry.section'
        db.add_column('cv_entry', 'section',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['cv.Section']),
                      keep_default=False)


        # Changing field 'Entry.related_project'
        db.alter_column('cv_entry', 'related_project_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Project'], null=True))

    def backwards(self, orm):
        # Deleting field 'Entry.section'
        db.delete_column('cv_entry', 'section_id')


        # Changing field 'Entry.related_project'
        db.alter_column('cv_entry', 'related_project_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['projects.Project']))

    models = {
        'cv.entry': {
            'Meta': {'object_name': 'Entry'},
            'date_end': ('django.db.models.fields.DateField', [], {}),
            'date_start': ('django.db.models.fields.DateField', [], {}),
            'desc': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'related_project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']", 'null': 'True', 'blank': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cv.Section']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'cv.section': {
            'Meta': {'object_name': 'Section'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'projects.project': {
            'Meta': {'object_name': 'Project'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['cv']