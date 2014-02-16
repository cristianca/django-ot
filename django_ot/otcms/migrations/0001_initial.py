# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CmsOtConfig'
        db.create_table(u'otcms_cmsotconfig', (
            (u'otconfig_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['django_ot.OtConfig'], unique=True, primary_key=True)),
            ('template', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('placeholder', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'otcms', ['CmsOtConfig'])


    def backwards(self, orm):
        # Deleting model 'CmsOtConfig'
        db.delete_table(u'otcms_cmsotconfig')


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
        u'otcms.cmsotconfig': {
            'Meta': {'object_name': 'CmsOtConfig', '_ormbases': [u'django_ot.OtConfig']},
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            u'otconfig_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['django_ot.OtConfig']", 'unique': 'True', 'primary_key': 'True'}),
            'placeholder': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['otcms']