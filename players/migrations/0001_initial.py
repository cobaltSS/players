# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Players'
        db.create_table(u'players_players', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('wins', self.gf('django.db.models.fields.IntegerField')()),
            ('lesions', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'players', ['Players'])


    def backwards(self, orm):
        # Deleting model 'Players'
        db.delete_table(u'players_players')


    models = {
        u'players.players': {
            'Meta': {'object_name': 'Players'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lesions': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'wins': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['players']