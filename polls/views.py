from django.shortcuts import get_object_or_404, render 
from django.http import HttpResponseRedirect, HttpResponse
from .models import Question, Choice, Vote
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login 
from django.conf import settings




def index(request):
    latest_question_list = Question.objects.order_by('-pup_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):

	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})



def results(request, question_id):

	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):

    user = request.user
    question = get_object_or_404(Question, pk=question_id)
    try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])


		Vote.objects.update_or_create(
        user=user,
        question=question,
        defaults={'selected_choice':selected_choice}
	    )

	    

    except (KeyError, Choice.DoesNotExist):

		return render(request, 'polls/detail.html',{

			'question': question ,
			'error_message': "you did't select any choice",

	    })


    else:

	    selected_choice.votes +=1
	    selected_choice.save()
	    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
   




def user_login(request):

	errors = []

	if request.method=='POST':

		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return	HttpResponseRedirect('/polls/')
			else:
				errors.append(" Sorry your acount is disapled")
				return render(request, 'polls/login.html', {'errors': errors})
		else:
			errors.append("invalid login details")
			return render(request, 'polls/login.html', {'errors': errors})
	else:
		return render(request, 'polls/login.html', {'errors': errors})

