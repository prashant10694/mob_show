from __future__ import unicode_literals

from django.db import models
from djangotoolbox.fields import EmbeddedModelField

# Create your models here.

class Smartphone(models.Model):
	name = models.CharField(max_length=200, db_index=True )
	technology = models.CharField(default='', blank=True, null=True, max_length= 100)
	launch = EmbeddedModelField('Launch')
	body = EmbeddedModelField('Body')
	display = EmbeddedModelField('Display')
	platform = EmbeddedModelField('Platform')
	memory = EmbeddedModelField('Memory')
	camera = EmbeddedModelField('Camera')
	sound = EmbeddedModelField('Sound')
	comms = EmbeddedModelField('Comms')
	features = EmbeddedModelField('Features')
	battery = models.CharField(default='', blank=True, null=True, max_length= 100)
	misc = 

class Launch(models.Model):
	announced = models.CharField()
	status = models.CharField()


class Body(models.Model):
	dimension = models.CharField()
	weight = models.CharField()
	build = models.CharField()
	sim_type = models.CharField()


class Display(models.Model):
	display_type = models.CharField()
	size = models.CharField()
	resolution = models.CharField()
	multitouch = models.CharField()
	protection = models.CharField()


class Platform(models.Model):
	os = models.CharField()
	chipset = models.CharField()
	cpu = models.CharField()
	gpu = models.CharField()


class Memory(models.Model):
	card_slot = models.CharField()
	internal = models.CharField()


class Camera(models.Model):
	primary = models.CharField()
	features = models.CharField()
	video = models.CharField()
	secondary = models.CharField()


class Sound(models.Model):
	alert_types = models.CharField()
	loudspeaker = models.CharField()
	jack = models.CharField()


class Comms(models.Model):
	wlan = models.CharField()
	bluetooth = models.CharField()
	gps = models.CharField()
	nfc = models.CharField()
	radio = models.CharField()
	usb = models.CharField()


class Features(models.Model):
	sensors = models.CharField()
	messaging = models.CharField()
	browser = models.CharField()
	java = models.CharField()
	extra = EmbeddedModelField('Extra')