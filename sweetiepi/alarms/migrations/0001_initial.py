# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RecurringAlarm'
        db.create_table(u'alarms_recurringalarm', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('time', self.gf('django.db.models.fields.TimeField')()),
            ('recurrences', self.gf('recurrence.fields.RecurrenceField')()),
        ))
        db.send_create_signal(u'alarms', ['RecurringAlarm'])

        # Adding model 'SingleAlarm'
        db.create_table(u'alarms_singlealarm', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'alarms', ['SingleAlarm'])


    def backwards(self, orm):
        # Deleting model 'RecurringAlarm'
        db.delete_table(u'alarms_recurringalarm')

        # Deleting model 'SingleAlarm'
        db.delete_table(u'alarms_singlealarm')


    models = {
        u'alarms.recurringalarm': {
            'Meta': {'object_name': 'RecurringAlarm'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'recurrences': ('recurrence.fields.RecurrenceField', [], {}),
            'time': ('django.db.models.fields.TimeField', [], {})
        },
        u'alarms.singlealarm': {
            'Meta': {'object_name': 'SingleAlarm'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['alarms']