from django.shortcuts import render_to_response, get_object_or_404
from survey.models import Poll
from django.http import Http404, HttpResponse



def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response('survey/index.html', {'latest_poll_list': latest_poll_list})

def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)