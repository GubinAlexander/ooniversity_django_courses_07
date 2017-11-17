from django.http import HttpResponse
from django.shortcuts import render
from .models import Question

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def hello(request):
	return render(request, "index.html")

def description(request):
    return render(request, "description.html")

def contact(request):
    return render(request, "contact.html")

def student_detail(request):
    return render(request, "student_detail.html")

def student_list(request):
    return render(request, "student_list.html")

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)