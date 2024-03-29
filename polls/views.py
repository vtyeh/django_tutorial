"""
In our poll application, we’ll have the following four views:

- Question “index” page – displays the latest few questions.
- Question “detail” page – displays a question text, with no results but with a form to vote.
- Question “results” page – displays results for a particular question.
- Vote action – handles voting for a particular choice in a particular question.

In Django, web pages and other content are delivered by views. Each view is represented by a 
simple Python function (or method, in the case of class-based views). Django will choose a view 
by examining the URL that’s requested (to be precise, the part of the URL after the domain name).
"""

from django.http import HttpResponseRedirect #HttpResponse, Http404
# from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.db.models import F

from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """ Return the last five published questions. """
        return Question.objects.order_by('-pub_date')[:5]
    
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    # Get the question
    question = get_object_or_404(Question, pk=question_id)

    try:
        # Get user's choice
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        # If no choice selected and form is submitted, redisplay the question voting form with error message
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })

    else:
        # Add 1 to the vote count of selected choice
        # Use F() to avoid race conditions. Database is responsible for updating,
        # so it only updates if a save() or update() is executed, rather than based 
        # on its value when the instance was retrieved
        selected_choice.votes = F('votes') + 1
        selected_choice.save()

    # Always return an HttpResponseRedirect after successfully dealing with POST data. 
    # This prevents data from being posted twice if a user hits the Back button.
    # reverse() helps to avoid having to hardcode a URL in the view function
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))