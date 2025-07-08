from django.shortcuts import render
from .models import Person, Passport, Reporter, Article, ModelFuel, CarModel


def person_list(request):
    people = Person.objects.all()
    return render(request, 'mvt/people.html', {'person_list': people})


def person_detail(request, pk):
    person = Person.objects.get(pk=pk)
    return render(request, 'mvt/person_detail.html', {'person': person})


def passport_list(request):
    passport = Passport.objects.all()
    return render(request, 'mvt/passport.html', {'passport_list': passport})


def passport_detail(request, pk):
    passport_number = Passport.objects.get(pk=pk)
    return render(request, 'mvt/passport_detail.html', {'passport_number': passport_number})


def reporter_list(request):
    reporter = Reporter.objects.all()
    return render(request, 'mvt/reporter_list.html', {'reporter_list': reporter})


def reporter_detail(request, pk):
    reporter = Reporter.objects.get(pk=pk)
    return render(request, 'mvt/reporter_detail.html', {'reporter': reporter})


def article_list(request):
    article = Article.objects.all()
    return render(request, 'mvt/article_list.html', {'article_list': article})


def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'mvt/article_detail.html', {'article': article})


def fuel_type_list(request):
    fuel_type = ModelFuel.objects.all()
    return render(request, 'mvt/fuel_type_list.html', {'fuel_type_list': fuel_type})


def fuel_type_detail(request, pk):
    fuel_type = ModelFuel.objects.get(pk=pk)
    return render(request, 'mvt/fuel_type_detail.html', {'fuel_type': fuel_type})


def carmodel_list(request):
    name = CarModel.objects.all()
    return render(request, 'mvt/carmodel_list.html', {'carmodel_list': name})


def carmodel_detail(request, pk):
    name = CarModel.objects.get(pk=pk)
    return render(request, 'mvt/carmodel_detail.html', {'carmodel': name})


def mvt(request):
    if request.method == 'GET':
        return render(request, 'mvt/mvt.html')
