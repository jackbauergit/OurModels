# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=32)
    passwd = models.CharField(max_length=32)
    login = models.CharField(max_length=32)
    #isActive = models.CharField(max_length=32)
    def __unicode__(self):
        return self.name

class Permission(models.Model):
    name = models.CharField(max_length=32)
    discribtion = models.TextField()
    def __unicode__(self):
        return self.name

class  UserPermissin(models.Model):
    user_id = models.IntegerField()
    Permission_id= models.IntegerField()
    delete = models.CharField(max_length=32)
    #如果delete=N 数据是有效的
    def __unicode__(self):
        return self.user_id
