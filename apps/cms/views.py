# coding=utf8

from django.template import RequestContext
from django.shortcuts import render_to_response

def home(request):
    return render_to_response('cms/default/home.html', {}, RequestContext(request))