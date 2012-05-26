from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user 	= 	models.ForeignKey(User, unique=True)
	address = 	models.CharField(max_length=255, blank=True)
	twitter = 	models.CharField(max_length=140, blank=True)
	github 	=	models.CharField(max_length=140, blank=True)
	url		=	models.CharField(max_length=140, blank=True)
	phone	=	models.CharField(max_length=20, blank=True)
	description = models.TextField(blank=True)
	def __unicode__(self):
		name = self.user
		return name.username
	
class Highlights(models.Model):
	profile = models.ForeignKey(Profile)
	description = models.TextField()
	class Meta:
		verbose_name_plural = "Highlights"
	def __unicode__(self):
		return self.description

class Skillset(models.Model):
	name = models.CharField(max_length=140)
	def __unicode__(self):
		return self.name

class Skills(models.Model):
	RATINGS = (
		('1','Beginner'),
		('2','Novice'),
		('3','Proficient'),
		('4','Strong'),
		('5','Expert'),
	)
	name = models.CharField(max_length=140)
	skillset = models.ForeignKey(Skillset)
	rating = models.CharField(max_length=1, choices=RATINGS)
	def __unicode__(self):
		return self.name
	class Meta:
		verbose_name_plural = "Skills"
		ordering = ['skillset','-rating','name']

class Job(models.Model):
	TYPES = (
		('p','Professional'),
		('v', 'Volunteer'),
	)
	company = models.CharField(max_length=50)
	type_of_job = models.CharField(max_length=1,choices=TYPES)
	start = models.DateField()
	end = models.DateField(blank=True, null=True)
	current = models.BooleanField()
	description = models.TextField()
	url = models.CharField(max_length=100, blank=True)
	def __unicode__(self):
		return self.company
	class Meta:
		ordering = ['type_of_job','-start']

class Position(models.Model):
	job = models.ForeignKey(Job)
	title = models.CharField(max_length=50)	
	start = models.DateField()
	end = models.DateField(blank=True)
	current = models.BooleanField()
	def __unicode__(self):
		return self.title
	
class Education(models.Model):
	degree = models.CharField(max_length=50)
	subject = models.CharField(max_length=50)
	date = models.DateField()
	school = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	in_progress = models.BooleanField()
	school_url = models.CharField(max_length=100, blank=True)
	def __unicode__(self):
		return self.degree + self.school
	class Meta:
		ordering = ['-date']

class ResumeVersion(models.Model):
	employer = models.CharField(max_length=100)
	updated = models.DateTimeField(auto_now=True)
	profile = models.ForeignKey(Profile)
	highlights = models.ManyToManyField(Highlights)
	skillset = models.ManyToManyField(Skillset)
	jobs = models.ManyToManyField(Job)
	education = models.ManyToManyField(Education)
	slug = models.SlugField(blank=True)
	def __unicode__(self):
		return self.employer