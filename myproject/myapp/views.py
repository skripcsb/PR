from django.shortcuts import render
from .models import Vacancy
from parser import parse_hh
def home(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        parse_hh(query)
    vacancies = Vacancy.objects.all()
    return render(request, 'myapp/home.html', {'vacancies': vacancies})

def search(request):
    query = request.GET.get('query')
    if query:
        vacancies = Vacancy.objects.filter(title__icontains=query)
    else:
        vacancies = Vacancy.objects.all()
