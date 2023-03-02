# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from .models import *

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


#Custom view for Projects
def display_prj(request):
    MODEL_HEADERS=[f.name for f in Project._meta.get_fields()]
    query_results = [list(i.values()) for i in list(Project.objects.all().values())]
    #return a response to your template and add query_results to the context
    return render(request, "home/projects_table.html", {
            "query_results" : query_results,
            "model_headers" : MODEL_HEADERS
        })

#Custom view for Owner
def display_own(request):
    MODEL_HEADERS=[f.name for f in Owner._meta.get_fields()]
    query_results = [list(i.values()) for i in list(Owner.objects.all().values())]
    #return a response to your template and add query_results to the context
    return render(request, "home/owners_table.html", {
            "query_results" : query_results,
            "model_headers" : MODEL_HEADERS
        })

#Custom view for requisite
def display_req(request):
    MODEL_HEADERS=[f.name for f in requisite._meta.get_fields()]
    query_results = [list(i.values()) for i in list(requisite.objects.all().values())]
    #return a response to your template and add query_results to the context
    return render(request, "home/requisites_table.html", {
            "query_results" : query_results,
            "model_headers" : MODEL_HEADERS
        })

#Custom view for tools
def display_tool(request):
    MODEL_HEADERS=[f.name for f in tool._meta.get_fields()]
    query_results = [list(i.values()) for i in list(tool.objects.all().values())]
    #return a response to your template and add query_results to the context
    return render(request, "home/tools_table.html", {
            "query_results" : query_results,
            "model_headers" : MODEL_HEADERS
        })


#Custom view for function
def display_funct(request):
    MODEL_HEADERS=[f.name for f in function._meta.get_fields()]
    query_results = [list(i.values()) for i in list(function.objects.all().values())]
    #return a response to your template and add query_results to the context
    return render(request, "home/functions_table.html", {
            "query_results" : query_results,
            "model_headers" : MODEL_HEADERS
        })

#Custom view for test
def display_test(request):
    MODEL_HEADERS=[f.name for f in test._meta.get_fields()]
    query_results = [list(i.values()) for i in list(test.objects.all().values())]
    #return a response to your template and add query_results to the context
    return render(request, "home/tests_table.html", {
            "query_results" : query_results,
            "model_headers" : MODEL_HEADERS
        })

#Custom view for questionnaire
def display_questionnaire(request):
    MODEL_HEADERS=[f.name for f in questionnaire._meta.get_fields()]
    query_results = [list(i.values()) for i in list(questionnaire.objects.all().values())]
    #return a response to your template and add query_results to the context
    return render(request, "home/questionnaire_table.html", {
            "query_results" : query_results,
            "model_headers" : MODEL_HEADERS
        })

#Custom view for Central dashboard
def display_centralDash(request):
    return render (request,"home/sPYCY_dash.html")
