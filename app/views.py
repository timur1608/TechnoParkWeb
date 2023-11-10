from django.shortcuts import render
from django.core.paginator import Paginator

QUESTIONS = [
        {
            'id': i,
            'title': f"Question {i}",
            'content': f'Long lorem ipsum {i}'
        } for i in range(20)
    ]

def paginate(objects, page, per_page=15):
    paginator = Paginator(objects, per_page)
    return paginator.page(page)
# Create your views here.
def index(request):
    page = request.GET.get('page', 1)
    return render(request, template_name='index.html', context= {'questions': paginate(QUESTIONS, page)})

def question(request, question_id):
    item = QUESTIONS[question_id]
    return render(request, template_name='question.html', context={'question': item})

def ask(request):
    return render(request, template_name='ask.html')

def signup(request):
    return render(request, template_name='signup.html')

def login(request):
    return render(request, template_name='login.html')

def tag(request):
    return render(request, template_name='tag.html')

def settings(request):
    return render(request, template_name='settings.html')