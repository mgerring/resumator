# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Profile'
        db.create_table('data_profile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=140, blank=True)),
            ('github', self.gf('django.db.models.fields.CharField')(max_length=140, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=140, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('data', ['Profile'])

        # Adding model 'Highlights'
        db.create_table('data_highlights', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.Profile'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('data', ['Highlights'])

        # Adding model 'Skillset'
        db.create_table('data_skillset', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=140)),
        ))
        db.send_create_signal('data', ['Skillset'])

        # Adding model 'Skills'
        db.create_table('data_skills', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('skillset', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.Skillset'])),
            ('rating', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('data', ['Skills'])

        # Adding model 'Job'
        db.create_table('data_job', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('type_of_job', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('start', self.gf('django.db.models.fields.DateField')()),
            ('end', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('current', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('data', ['Job'])

        # Adding model 'Position'
        db.create_table('data_position', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('job', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.Job'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('start', self.gf('django.db.models.fields.DateField')()),
            ('end', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('current', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('data', ['Position'])

        # Adding model 'Education'
        db.create_table('data_education', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('degree', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('school', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('in_progress', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('school_url', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('data', ['Education'])

        # Adding model 'ResumeVersion'
        db.create_table('data_resumeversion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('employer', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.Profile'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, blank=True)),
        ))
        db.send_create_signal('data', ['ResumeVersion'])

        # Adding M2M table for field highlights on 'ResumeVersion'
        db.create_table('data_resumeversion_highlights', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('resumeversion', models.ForeignKey(orm['data.resumeversion'], null=False)),
            ('highlights', models.ForeignKey(orm['data.highlights'], null=False))
        ))
        db.create_unique('data_resumeversion_highlights', ['resumeversion_id', 'highlights_id'])

        # Adding M2M table for field skillset on 'ResumeVersion'
        db.create_table('data_resumeversion_skillset', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('resumeversion', models.ForeignKey(orm['data.resumeversion'], null=False)),
            ('skillset', models.ForeignKey(orm['data.skillset'], null=False))
        ))
        db.create_unique('data_resumeversion_skillset', ['resumeversion_id', 'skillset_id'])

        # Adding M2M table for field jobs on 'ResumeVersion'
        db.create_table('data_resumeversion_jobs', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('resumeversion', models.ForeignKey(orm['data.resumeversion'], null=False)),
            ('job', models.ForeignKey(orm['data.job'], null=False))
        ))
        db.create_unique('data_resumeversion_jobs', ['resumeversion_id', 'job_id'])

        # Adding M2M table for field education on 'ResumeVersion'
        db.create_table('data_resumeversion_education', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('resumeversion', models.ForeignKey(orm['data.resumeversion'], null=False)),
            ('education', models.ForeignKey(orm['data.education'], null=False))
        ))
        db.create_unique('data_resumeversion_education', ['resumeversion_id', 'education_id'])

    def backwards(self, orm):
        # Deleting model 'Profile'
        db.delete_table('data_profile')

        # Deleting model 'Highlights'
        db.delete_table('data_highlights')

        # Deleting model 'Skillset'
        db.delete_table('data_skillset')

        # Deleting model 'Skills'
        db.delete_table('data_skills')

        # Deleting model 'Job'
        db.delete_table('data_job')

        # Deleting model 'Position'
        db.delete_table('data_position')

        # Deleting model 'Education'
        db.delete_table('data_education')

        # Deleting model 'ResumeVersion'
        db.delete_table('data_resumeversion')

        # Removing M2M table for field highlights on 'ResumeVersion'
        db.delete_table('data_resumeversion_highlights')

        # Removing M2M table for field skillset on 'ResumeVersion'
        db.delete_table('data_resumeversion_skillset')

        # Removing M2M table for field jobs on 'ResumeVersion'
        db.delete_table('data_resumeversion_jobs')

        # Removing M2M table for field education on 'ResumeVersion'
        db.delete_table('data_resumeversion_education')

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'data.education': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Education'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'degree': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_progress': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'school_url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'data.highlights': {
            'Meta': {'object_name': 'Highlights'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.Profile']"})
        },
        'data.job': {
            'Meta': {'ordering': "['type_of_job', '-start']", 'object_name': 'Job'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'end': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.DateField', [], {}),
            'type_of_job': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'data.position': {
            'Meta': {'object_name': 'Position'},
            'current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.Job']"}),
            'start': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'data.profile': {
            'Meta': {'object_name': 'Profile'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'github': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'data.resumeversion': {
            'Meta': {'object_name': 'ResumeVersion'},
            'education': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['data.Education']", 'symmetrical': 'False'}),
            'employer': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'highlights': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['data.Highlights']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jobs': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['data.Job']", 'symmetrical': 'False'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.Profile']"}),
            'skillset': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['data.Skillset']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'data.skills': {
            'Meta': {'ordering': "['skillset', '-rating', 'name']", 'object_name': 'Skills'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'rating': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'skillset': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.Skillset']"})
        },
        'data.skillset': {
            'Meta': {'object_name': 'Skillset'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        }
    }

    complete_apps = ['data']