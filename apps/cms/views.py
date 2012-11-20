# coding=utf8

from django.template import RequestContext
from django.shortcuts import render_to_response, get_list_or_404
from apps.cms.models import Project, Client, Carousel

def home(request):
    carousels = get_list_or_404(Carousel)

    return render_to_response('cms/default/home.html', {'carousels': carousels}, RequestContext(request))

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
