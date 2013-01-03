# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Board'
        db.create_table('app_board', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='255')),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('app', ['Board'])

        # Adding field 'Link.board'
        db.add_column('app_link', 'board',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['app.Board']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Board'
        db.delete_table('app_board')

        # Deleting field 'Link.board'
        db.delete_column('app_link', 'board_id')


    models = {
        'app.board': {
            'Meta': {'object_name': 'Board'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"})
        },
        'app.link': {
            'Meta': {'object_name': 'Link'},
            'board': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.Board']"}),
            'data': ('django.db.models.fields.TextField', [], {}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'url': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['app']