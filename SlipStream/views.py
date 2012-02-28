from django.contrib.auth.views import login
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    c = RequestContext(request)
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home/')
    else:
        return render_to_response('index.html',c)

