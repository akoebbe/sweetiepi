# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ClockStyle'
        db.create_table(u'clocks_clockstyle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('dial', self.gf('django.db.models.fields.CharField')(default='din 41091.4', max_length=100)),
            ('hourHand', self.gf('django.db.models.fields.CharField')(default='din 41092.3', max_length=100)),
            ('minuteHand', self.gf('django.db.models.fields.CharField')(default='din 41092.3', max_length=100)),
            ('secondHand', self.gf('django.db.models.fields.CharField')(default='din 41071.1', max_length=100)),
            ('minuteHandBehavior', self.gf('django.db.models.fields.CharField')(default='sweeping', max_length=100)),
            ('secondHandBehavior', self.gf('django.db.models.fields.CharField')(default='stepping', max_length=100)),
            ('secondHandStopToGo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('secondHandStopTime', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('backgroundColor', self.gf('django.db.models.fields.CharField')(default='0,0,0,0', max_length=20)),
            ('dialColor', self.gf('django.db.models.fields.CharField')(default='255,255,255', max_length=11)),
            ('hourHandColor', self.gf('django.db.models.fields.CharField')(default='0,0,0', max_length=11)),
            ('minuteHandColor', self.gf('django.db.models.fields.CharField')(default='0,0,0', max_length=11)),
            ('secondHandColor', self.gf('django.db.models.fields.CharField')(default='0,0,0', max_length=11)),
            ('axisCoverColor', self.gf('django.db.models.fields.CharField')(default='0,0,0', max_length=11)),
            ('axisCoverRadius', self.gf('django.db.models.fields.PositiveIntegerField')(default=7)),
            ('updateInterval', self.gf('django.db.models.fields.PositiveIntegerField')(default=50)),
        ))
        db.send_create_signal(u'clocks', ['ClockStyle'])


    def backwards(self, orm):
        # Deleting model 'ClockStyle'
        db.delete_table(u'clocks_clockstyle')


    models = {
        u'clocks.clockstyle': {
            'Meta': {'object_name': 'ClockStyle'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'axisCoverColor': ('django.db.models.fields.CharField', [], {'default': "'0,0,0'", 'max_length': '11'}),
            'axisCoverRadius': ('django.db.models.fields.PositiveIntegerField', [], {'default': '7'}),
            'backgroundColor': ('django.db.models.fields.CharField', [], {'default': "'0,0,0,0'", 'max_length': '20'}),
            'dial': ('django.db.models.fields.CharField', [], {'default': "'din 41091.4'", 'max_length': '100'}),
            'dialColor': ('django.db.models.fields.CharField', [], {'default': "'255,255,255'", 'max_length': '11'}),
            'hourHand': ('django.db.models.fields.CharField', [], {'default': "'din 41092.3'", 'max_length': '100'}),
            'hourHandColor': ('django.db.models.fields.CharField', [], {'default': "'0,0,0'", 'max_length': '11'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minuteHand': ('django.db.models.fields.CharField', [], {'default': "'din 41092.3'", 'max_length': '100'}),
            'minuteHandBehavior': ('django.db.models.fields.CharField', [], {'default': "'sweeping'", 'max_length': '100'}),
            'minuteHandColor': ('django.db.models.fields.CharField', [], {'default': "'0,0,0'", 'max_length': '11'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'secondHand': ('django.db.models.fields.CharField', [], {'default': "'din 41071.1'", 'max_length': '100'}),
            'secondHandBehavior': ('django.db.models.fields.CharField', [], {'default': "'stepping'", 'max_length': '100'}),
            'secondHandColor': ('django.db.models.fields.CharField', [], {'default': "'0,0,0'", 'max_length': '11'}),
            'secondHandStopTime': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'secondHandStopToGo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updateInterval': ('django.db.models.fields.PositiveIntegerField', [], {'default': '50'})
        }
    }

    complete_apps = ['clocks']