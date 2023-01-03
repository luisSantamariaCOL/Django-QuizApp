from django.shortcuts import render
from .models import Question


# Create your views here.
def index(request):
    question = Question.get_objects()
    print("Questions: " + question)

    return render(request, 'polls/index.html')