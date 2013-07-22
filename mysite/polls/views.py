# Create your views here.
from django.http import HttpResponse
from polls.models import Poll
from django.shortcuts import render, get_object_or_404

def index(request):
    latest_polls = Poll.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = RequestContext(request, {
    #     'latest_poll_list': latest_polls,
    # })
    # return HttpResponse(template.render(context))
    return render(request, 'polls/index.html', {'latest_poll_list': latest_polls})

def detail(request, poll_id):
    # try:
    #     poll = Poll.objects.get(pk=poll_id)
    # except Poll.DoesNotExist:
    #     raise Http404

    poll = get_object_or_404(Poll, pk=poll_id)

    return render(request, 'polls/detail.html', {'poll': poll})

def results(request, poll_id):
    return HttpResponse("this is results of poll id %s" % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll id %s" % poll_id)
