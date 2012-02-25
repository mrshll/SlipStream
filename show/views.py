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
    form=AddShowForm()
    return render_to_response('home.html', {'user': request.user,
                                            'userprofile': user_profile,
                                            'form': form,
    }, context_instance=RequestContext(request))

@login_required
def add(request):
    result = {'bad':'false'}
    user_profile = request.user.get_profile()
    if request.method == 'POST':
        form=AddShowForm(request.POST)
        if not form.is_valid():
            result.update({'bad':'true'})
            d={}
            for e in form.errors.iteritems():
                d.update({e[0]:unicode(e[1])})
            result.update({'errs': d })
        s = Show(name=form.cleaned_data['show_name'])
        s.save()
        user_profile.shows.add(s)

    json = simplejson.dumps(result, ensure_ascii=False)
    return HttpResponse( json, mimetype='application/javascript' )


