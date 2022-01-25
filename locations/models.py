from django.db import models
from django_countries.fields import CountryField
# Create your models here.
class Province(models.Model):
	provincecode = models.IntegerField(primary_key = True)
	provincename = models.CharField(max_length = 100)

	class Meta:
		db_table = "provincetable"


class District(models.Model):
	districtCode = models.IntegerField( primary_key = True)
	districtname = models.CharField(max_length = 100)
	provincecode = models.IntegerField()

	class Meta:
		db_table = "districttable"

class Sector(models.Model):
	sectorID = models.IntegerField( primary_key = True)
	sectorname = models.CharField(max_length = 100)
	districtCode = models.IntegerField()
	provincecode = models.IntegerField()

	class Meta:
		db_table = "sectortable"


class Cell(models.Model):
	cellID = models.IntegerField( primary_key = True)
	cellname = models.CharField(max_length = 100)
	sectorID = models.IntegerField()
	districtCode = models.IntegerField()
	provincecode = models.IntegerField()

	class Meta:
		db_table = "celltable"

class Village(models.Model):
	villageID = models.IntegerField( primary_key = True)
	villagename = models.CharField(max_length = 100)
	cellID = models.IntegerField()
	sectorID = models.IntegerField()
	districtCode = models.IntegerField()
	provincecode = models.IntegerField()

	class Meta:
		db_table = "villagetable"		