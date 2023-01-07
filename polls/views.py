from django.shortcuts import render
from .models import Question


# Create your views here.
def index(request):
    latest_question_list = Question.objects.all()
    return render(request, 'polls/index.html', {
        "latest_question_list": latest_question_list,
    })

def detail(request, question_id):
    return render(request, 'polls/detail.html', {'question_id': question_id})

def results(request, question_id):
    return render(request, 'polls/results.html', {'question_id': question_id})

def vote(request, question_id):
    return render(request, 'polls/vote.html', {'question_id': question_id})