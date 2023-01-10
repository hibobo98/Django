from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

# view를 호출하려면 연결된 URL이 있어야함! > urls.py로 이동

def detail(request, question_id):
    return HttpResponse("you're looking at %s" % question_id)

def results(request, question_id):
    response='you are looking at result %s'
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("you're voting on %s" % question_id)