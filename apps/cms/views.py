from django.template import RequestContext

__author__ = 'hthieu1110'
# coding=utf8

from django.shortcuts import render_to_response

def home(request):
    return render_to_response('base.html', {}, RequestContext(request))