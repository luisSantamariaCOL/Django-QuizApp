from django.shortcuts import render, get_object_or_404
from .models import Question


# Create your views here.
def index(request):
    latest_question_list = Question.objects.all()
    return render(request, 'polls/index.html', {
        "latest_question_list": latest_question_list,
    })

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()
    return render(request, 'polls/detail.html', {'question': question, 'choices': choices})

def results(request, question_id):
    return render(request, 'polls/results.html', {'question_id': question_id})

def vote(request, question_id):
    return render(request, 'polls/vote.html', {'question_id': question_id})