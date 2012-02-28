from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.utils import simplejson
from show.forms import AddShowForm
from show.models import Show

@login_required
def home(request):
    user_profile = request.user.get_profile()
    return render_to_response('home.html', {'user': request.user,
                                            'userprofile': user_profile,
    }, context_instance=RequestContext(request))

#def get(request, id):
#    show = Show.objects.

@login_required
def add(request):
    if request.POST and request.POST.get('show_name'):
        new_show = Show.objects.get(name=request.POST.get('show_name'))
        request.user.get_profile().shows.add(new_show)
        return HttpResponse(new_show.name)
    return HttpResponse("")

@login_required
def lookup(request):
    # Default return list
    results = []
    if request.method == "GET":
        if request.GET.has_key(u'query'):
            value = request.GET[u'query']
            # Ignore queries shorter than length 3
            if len(value) > 2:
                model_results = Show.objects.filter(name__startswith=value)
                results = [ x.name for x in model_results ]
    json = simplejson.dumps(results)
    return HttpResponse(json, mimetype='application/json')

