# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OtNews'
        db.create_table(u'django_ot_otnews', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ot_config', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_ot.OtConfig'])),
            ('ot_news_pk', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('hash', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'django_ot', ['OtNews'])


    def backwards(self, orm):
        # Deleting model 'OtNews'
        db.delete_table(u'django_ot_otnews')


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
        },
        u'django_ot.otnews': {
            'Meta': {'object_name': 'OtNews'},
            'hash': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ot_config': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_ot.OtConfig']"}),
            'ot_news_pk': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['django_ot']