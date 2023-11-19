from django.shortcuts import render
from django.core.paginator import Paginator
from app.models import Profile, Question
from django.http import HttpResponse

QUESTIONS = [
    {
        'id': i,
        'title': f"Question {i}",
        'text': f'Long lorem ipsum {i}',
        'tags': ['dz1', 'lorem']
    } for i in range(30)
]


def paginate(objects, request, per_page=10):
    paginator = Paginator(objects, per_page)
    page = request.GET.get('page', 1)
    if str(page).isdigit() and int(page) <= int(len(QUESTIONS) / per_page):
        return paginator.page(page)
    return paginator.page(1)


# Create your views here.

def index(request):
    questions = Question.objects.order_by("date_written")
    return render(request, template_name='index.html', context={'questions': paginate(questions, request)})


def question(request, question_id):
    item = Question.objects.match(question_id)[0]
    return render(request, template_name='question.html', context={'question': item})


def ask(request):
    return render(request, template_name='ask.html')


def signup(request):
    items = ['Login', 'Email', 'NickName', 'Password', 'Repeat Password']

    return render(request, template_name='signup.html', context={'blocks': items})


def login(request):
    items = ['Login', 'Password']
    return render(request, template_name='login.html', context={'blocks': items})


def tag(request, label):
    questions = Question.objects.tag_questions(label)
    if (len(questions) == 0):
        return render(request, '404.html', status=404)
    else:
        return render(request, template_name='tag.html',
                      context={'questions': paginate(questions[0].questions.all(), request), 'tag': label})


def settings(request):
    blocks = ['Login', ]
    return render(request, template_name='settings.html', context={'blocks': blocks})


def hot(request):
    questions = Question.objects.top5()
    return render(request, template_name='hot.html', context={'questions': paginate(questions, request)})
