from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Question

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
	response = "You are looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)


"""
Context is a dictionary mapping template variable names to Python objects.

The render() function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument. It returns an HttpResponse object of the given template rendered with the given context.

"""