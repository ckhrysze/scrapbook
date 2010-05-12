# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'BlogEntry'
        db.create_table('sbmain_blogentry', (
            ('entry', self.gf('django.db.models.fields.TextField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('sbmain', ['BlogEntry'])

        # Adding model 'Gallery'
        db.create_table('sbmain_gallery', (
            ('path', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('sbmain', ['Gallery'])

        # Adding model 'PortraitGallery'
        db.create_table('sbmain_portraitgallery', (
            ('path', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('sbmain', ['PortraitGallery'])

        # Adding model 'ImageRef'
        db.create_table('sbmain_imageref', (
            ('gallery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sbmain.Gallery'])),
            ('filename', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('sbmain', ['ImageRef'])

        # Adding model 'PortraitRef'
        db.create_table('sbmain_portraitref', (
            ('gallery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sbmain.PortraitGallery'])),
            ('filename', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('sbmain', ['PortraitRef'])

        # Adding model 'VideoRef'
        db.create_table('sbmain_videoref', (
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('filename', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('sbmain', ['VideoRef'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'BlogEntry'
        db.delete_table('sbmain_blogentry')

        # Deleting model 'Gallery'
        db.delete_table('sbmain_gallery')

        # Deleting model 'PortraitGallery'
        db.delete_table('sbmain_portraitgallery')

        # Deleting model 'ImageRef'
        db.delete_table('sbmain_imageref')

        # Deleting model 'PortraitRef'
        db.delete_table('sbmain_portraitref')

        # Deleting model 'VideoRef'
        db.delete_table('sbmain_videoref')
    
    
    models = {
        'sbmain.blogentry': {
            'Meta': {'object_name': 'BlogEntry'},
            'entry': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'sbmain.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'sbmain.imageref': {
            'Meta': {'object_name': 'ImageRef'},
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sbmain.Gallery']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'sbmain.portraitgallery': {
            'Meta': {'object_name': 'PortraitGallery'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'sbmain.portraitref': {
            'Meta': {'object_name': 'PortraitRef'},
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sbmain.PortraitGallery']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'sbmain.videoref': {
            'Meta': {'object_name': 'VideoRef'},
            'desc': ('django.db.models.fields.TextField', [], {}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }
    
    complete_apps = ['sbmain']
