from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse

from .models import Choice, Question
from .forms import NameForm
import json


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

def get_name(request):
    #if request.method == 'GET':
    #    return render(request, 'polls/search.html')
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        concat = request.POST
        subject = request.body
        #form = NameForm(request.POST)
        rtpreport_dir_f = "/home/tq/py_env/django/mysite/polls/t1.txt"
        #subject = form.cleaned_data['your_name']
        json_result = json.loads(subject)
        subject = json_result['your_name']
        with open(rtpreport_dir_f, "a") as f:
            f.write(subject + "\n")
        return HttpResponse("Hello, world. You're at the polls index.")
        # check whether it's valid:
        #if form.is_valid():
        #    rtpreport_dir_f = "/home/tq/py_env/django/mysite/polls/t1.txt"
        #    subject = form.cleaned_data['your_name']
        #    with open(rtpreport_dir_f, "a") as f:
        #        f.write(subject + "\n")
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('/thanks/')
        #    return render(request, 'polls/search.html', {'form':form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'polls/name.html', {'form': form})

