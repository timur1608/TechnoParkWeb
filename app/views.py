from django.shortcuts import render
from django.core.paginator import Paginator

QUESTIONS = [
    {
        'id': i,
        'title': f"Question {i}",
        'content': f'Long lorem ipsum {i}',
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
    return render(request, template_name='index.html', context={'questions': paginate(QUESTIONS, request)})


def question(request, question_id):
    item = QUESTIONS[question_id]
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
    return render(request, template_name='tag.html', context={'questions': paginate(QUESTIONS, request), 'tag': label})


def settings(request):
    blocks = ['Login', ]
    return render(request, template_name='settings.html', context={'blocks': blocks})


def hot(request):
    return render(request, template_name='hot.html', context={'questions': paginate(QUESTIONS, 1)})
