# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
import datetime
from django.utils import timezone

from .custom.database import *


class questionnaire(models.Model):
    area = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    question = models.TextField()
    note = models.TextField()
    typology = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
        
    def get_question(self):
        return self.question

class function(models.Model):
   
    name = models.CharField(max_length=50)
    sec_function = models.CharField(max_length=150)
    description = models.TextField()
    area = models.CharField(max_length=50)
    subarea = models.CharField(max_length=50)

    def __str__(self):
       return self.name
		
    def get_description(self):
       return self.description

class test(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
	
    def get_description(self):
        return self.description

class tool(models.Model):
    SSA = models.CharField(max_length=15)
    funct_referent = models.CharField(max_length=50)
    tech_referent = models.CharField(max_length=50)
    acronym = models.CharField(max_length=15)
    product_id = models.CharField(max_length=15)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    subarea = models.CharField(max_length=50)
    description = models.TextField()
    enduser = models.CharField(max_length=50)
    end_of_life = models.DateField(null=True,blank=True)
    end_of_support = models.DateField(null=True,blank=True)
    vendor = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    DR = models.CharField(max_length=50)
    HA = models.CharField(max_length=50)
    DRHA_solution = models.CharField(max_length=70)
    RTO = models.CharField(max_length=50)
    last_update = models.DateField(null=True,blank=True)
    sec_function = models.TextField()
    
    def __str__(self):
        return self.name

    def get_description(self):
        return self.description

class requisite(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    typology = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_description(self):
        return self.description


class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=50)
    full_name = models.CharField(max_length=70, unique=True, blank=True)

    def __str__(self):
        return self.full_name

class Project(models.Model):
    name = models.CharField(max_length=50)
    publish_date = models.DateField('date_published')
    elapsed_months = models.IntegerField()
    owner = models.ForeignKey(Owner, to_field='full_name', on_delete=models.SET('Unmanaged'), default='Unmanaged')
    effort = models.IntegerField()
    evaluation = models.CharField(max_length=50,default="Detailed")
    status = models.CharField(max_length=50,default="Open")
    risk = models.IntegerField(default=0)
    approval = models.CharField(max_length=20,default="Not Approved")

    def __str__(self):
        return self.name

    def published_date(self):
        return self.publish_date

    #create new project	
    def create(cls,newName,newPub,newOwn,newElap):
        db_conn= db_connect()
        prjList= db_getlist("name","home_project",db_conn)
        ownList= db_getlist("owner","home_project",db_conn)
	    #check if already exists
        if newName in prjList:
            #error mgmt to be added
            print("ERROR: Project already existing")
            return None
            #check if prj owner exist
        elif newOwn in ownList:
            #create new line in home_project
            newPrj = cls(name=newName,publish_date=newPub,owner=newOwn,elapsed_months=newElap)
            #create and populate new prj specific questionnaire 
            db_create_prj_quest(newName, db_conn)
            #create and kickstart new prj specific timeline
            db_create_prj_timeline(newName, db_conn)
            return newPrj
        else:
            #error mgmt to be added
            print("ERROR: Owner not existing")
            return None
