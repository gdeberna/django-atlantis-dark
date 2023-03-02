# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [
    # Projects Url
    path('Projects', views.display_prj, name='Projects'),

    # Owners Url
    path('Owners', views.display_own, name='Owners'),

    # requirements Url
    path('requirements', views.display_req, name='requirements'),

    # tools Url
    path('tools', views.display_tool, name='tools'),

    # functions Url
    path('functions', views.display_funct, name='functions'),

    # test Url
    path('tests', views.display_test, name='tests'),

    # questionnaire Url
    path('questionnaire', views.display_questionnaire, name='questionnaire'),
    
    # Central Dashboard Url
    path('spycy_dash', views.display_centralDash, name='spycy_dash'),
    
    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
