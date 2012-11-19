# coding=utf8
from django.core.urlresolvers import resolve

class ViewMiddleware():
    def process_request(self, request):
        request.view_name = resolve(request.path).url_name
        return None