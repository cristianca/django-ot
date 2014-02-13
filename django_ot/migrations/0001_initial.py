# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OtAccount'
        db.create_table(u'django_ot_otaccount', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('user', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('api_key', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'django_ot', ['OtAccount'])

        # Adding model 'OtConfig'
        db.create_table(u'django_ot_otconfig', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_ot.OtAccount'])),
            ('channel', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'django_ot', ['OtConfig'])


    def backwards(self, orm):
        # Deleting model 'OtAccount'
        db.delete_table(u'django_ot_otaccount')

        # Deleting model 'OtConfig'
        db.delete_table(u'django_ot_otconfig')


    models = {
        u'django_ot.otaccount': {
            'Meta': {'object_name': 'OtAccount'},
            'api_key': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'django_ot.otconfig': {
            'Meta': {'object_name': 'OtConfig'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_ot.OtAccount']"}),
            'action': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'channel': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['django_ot']