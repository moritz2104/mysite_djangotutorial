from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse

from .models import Question, Choicex

def index(request):
	letzte_fragen_liste = Question.objects.order_by('-pub_date')[:5]
	# output fliegt raus, stattdessen gibt es jetzt das template.
	# output = ', '.join([i.question_text for i in letzte_fragen_liste])
	context = {'letzte_fragen_liste': letzte_fragen_liste}
	return render (request, 'polls/index.html', context)

def detail(request, question_id):
	question = get_object_or_404(Question, pk = question_id) 
	context = {'question': question}
	return render(request, 'polls/detail.html', context)

def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question': question})

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