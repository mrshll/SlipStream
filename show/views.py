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

@logi_required
def add(request):
    if request.POST and request.POST.get('show_name'):
        new_show = Show(name=request.POST.get('show_name'))
        new_show.save()
        request.user.get_profile().show.add(new_show)
        xhtml = render_bbcode(request.POST.get('text'))

'''
@login_required
def add(request):
    if not request.POST:
        return render_to_response('index.html', {})
    xhr = request.GET.has_key('xhr')
    response_dict = {}
    show_name = request.POST.get('show_name', False)
    total = request.POST.get('total', False)
    response_dict.update({'name': show_name, 'total': total})
    if request.show_name:
        response_dict.update({'success': True})
        print(request,response_dict)
        #s = Show(name=form.cleaned_data['show_name'])
        #s.save()
    else:
        response_dict.update({'errors': {}})
        if not show_name:
            response_dict['errors'].update({'show_name': 'This field is required'})
    if xhr:
        return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
    return render_to_response('index.html', response_dict)
