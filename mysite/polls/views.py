from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect 
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import RequestContext, loader 

from .models import Question, Choice 

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'
	def get_queryset(self):
		"""Return the last five published questions"""
		return Questions.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'
	
""" Old way of presenting views (without generic views)
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {
		'latest_question_list': latest_question_list
		}
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question':question})
"""
def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		#request.POST is a dictionary-like object allowing access to submitted
		#data by key name. request.POST vals are always strings
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		#KeyError if 'choice' not in request.POST
		#Redisplay the question voting form
		return render(request, 'polls/detail.html',
			{'question':question, 'error_message': "You didn't select a choice"})
	else: 
		selected_choice.votes+=1
		selected_choice.save()
		#Always return an HttpResponseRedirect after successfully dealing
		#with POST data. This stops data from being posted twice if a 
		#user hits the back button
		#reverse helps avoid us hardcoding a URL, returns a HttpRequest object
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))