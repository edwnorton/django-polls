from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse
from datetime import datetime
from .models import Choice, Question
from .forms import NameForm
import json
import logging

a = "http://django.ismartcloud.com.cn:18080/polls/search"

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def download(request):
    if request.method == 'GET':
        url = request.body
        return HttpResponseRedirect(a)
        #return HttpResponse("1111")

def ttime(request):
    rtpreport_dir_f = "/home/tq/py_env/django/mysite/polls/t1.txt"
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            ip = form.cleaned_data['ip']
            begintime = form.cleaned_data['begintime']
            begintime = begintime.strftime("%Y/%m/%d %H:%M")
            endtime = form.cleaned_data['endtime']
            endtime = endtime.strftime("%Y/%m/%d %H:%M")
            port = form.cleaned_data['port']
            with open(rtpreport_dir_f, "a") as f:
                f.write(ip + "," + begintime + "," + endtime + "," + port)
            a = "点击下载"
            return render(request, 'polls/download.html', {'downurl':a})
    else:
        form = NameForm
    return render(request, 'polls/timetest.html', {'form': form})

def get_name(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        concat = request.POST
        subject = request.body
        form = NameForm(request.POST)
        rtpreport_dir_f = "/home/tq/py_env/django/mysite/polls/t1.txt"
        #subject = form.cleaned_data['your_name']
        #json_result = json.loads(subject)
        #subject = json_result['your_name']
        #with open(rtpreport_dir_f, "a") as f:
        #    f.write(subject + "\n")
        #return HttpResponse("Hello, world. You're at the polls index.")
        # check whether it's valid:
        if form.is_valid():
            rtpreport_dir_f = "/home/tq/py_env/django/mysite/polls/t1.txt"
            ip = form.cleaned_data['ip']
            begintime = form.cleaned_data['begintime']
            endtime = form.cleaned_data['endtime']
            port = form.cleaned_data['port']
            with open(rtpreport_dir_f, "a") as f:
                f.write(ip + "," + begintime + "," + endtime + "," + port)
            a = "http://30.48.196.10:8000/test"
            # redirect to a new URL:
            # return HttpResponseRedirect("30.")
            #return HttpResponse("{0},{1},{2},{3}".format(ip, begintime, endtime, port))
            return render(request, 'polls/download.html', {'downurl':a})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'polls/name.html', {'form': form})

