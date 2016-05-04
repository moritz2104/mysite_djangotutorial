from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
	# /polls/
	url(r'^$', views.index, name='index'), 
	# /polls/5/ # the 'name' value as called by the {% url %} template tag
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	# /polls/5/results/
	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
	# /polls/5/vote/
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]	

# url() nimmt vier arguments: (regex, view, kwags, name)
# regex & view sind required, kwargs und name nicht
# name vergibt einen Namen, so dass dieser von anderswo angesteuert werden kann