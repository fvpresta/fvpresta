# coding=utf8

from django.template import RequestContext
from django.shortcuts import render_to_response
from apps.cms.models import Project, Client

def home(request):
    return render_to_response('cms/default/home.html', {}, RequestContext(request))

def clients(request):
    clients = Client.objects.all()

    return render_to_response('cms/default/clients.html', {
        'clients': clients,
        }, RequestContext(request))

def portfolio(request):
    projects = Project.objects.all()

    return render_to_response('cms/default/portfolio.html', {
        'projects': projects,
    }, RequestContext(request))

def aboutUs(request):
    return render_to_response('cms/default/about_us.html', {}, RequestContext(request))

def contact(request):
    return render_to_response('cms/default/contact.html', {}, RequestContext(request))
