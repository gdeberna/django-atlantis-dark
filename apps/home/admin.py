# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import * 
# Register your models here.

admin.site.register(Project)
admin.site.register(Owner)
admin.site.register(requisite)
admin.site.register(tool)
admin.site.register(function)
admin.site.register(test)
admin.site.register(questionnaire)
