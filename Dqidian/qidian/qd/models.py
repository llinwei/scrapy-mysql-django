# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Qidian(models.Model):
    bname = models.CharField(primary_key=True, max_length=20)
    bauthor = models.CharField(max_length=10, blank=True, null=True)
    btype = models.CharField(max_length=10, blank=True, null=True)
    bstate = models.CharField(max_length=7, blank=True, null=True)
    bimg = models.CharField(max_length=100, blank=True, null=True)
    burl = models.CharField(max_length=500, blank=True, null=True)
    bintro = models.CharField(max_length=500, blank=True, null=True)
    bauturl = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qidian'
