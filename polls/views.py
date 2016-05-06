from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choicex

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'letzte_fragen_liste'

	def get_queryset(self): # get_queryset ist für ListViews obligatorisch
		"""Return the last five published questions. (Not including those set to be published in the future.)"""
		x = Question.objects.filter(pub_date__lte=timezone.now())
		y = x.order_by('-pub_date')[:5]

		return y


class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

	def get_queryset(self):
		"""
		Excludes any questions that aren't published yet.
		"""
		return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

# VORHER WAR DAS SO:
# def results(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choicex_set.get(pk=request.POST['choice'])
	except (KeyError, Choicex.DoesNotExist):
		# Redisplay the question voting form
		return render(request, 'polls/detail.html', {
			'question': question, 
			'error_message': "You didn't select a choice, yo!",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.	
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


"""
Context is a dictionary mapping template variable names to Python objects.

The render() function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument. It returns an HttpResponse object of the given template rendered with the given context.

"""