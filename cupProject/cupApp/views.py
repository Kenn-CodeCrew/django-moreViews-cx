from django.shortcuts import render
from django.http import HttpResponse
from .models import Cup


# Create your views here.
def index(request):
    return HttpResponse("Test URL")

# HTML link
def cupindex(request):
    cup_list = Cup.objects.all()
    new_cups = Cup.objects.filter(manufactuerDate__gt='2012-01-01')
    context = {'allCups': cup_list,
               'newCups': new_cups
               }
    return render(request, 'cupApp/index.html', context)

# Ex 1 functions
def greeting(request, name):
    return HttpResponse('Hello ' + name)


def multiply(request, number):
    return HttpResponse('The product times 2 is:  ' + str(number*2))


def add(request, mytotal):
    sum = 0
    for x in range(mytotal + 1):
        sum += x

    return HttpResponse('The sum of all numbers from 0 to the integer is: ' + str(sum))

# Ex 2 functions
def addcup1(request):
    newCup = Cup.objects.create(name='Wine Glass', material='glass', manufactuerDate='2017-02-01')
    return HttpResponse('check the admin')


def addcup2(request):
    newCup = Cup(name='Mug', material='ceramic', manufactuerDate='2019-02-01')
    newCup.save()
    return HttpResponse('check the admin')


def all(request):
    cups = Cup.objects.all()
    newstring = ""
    for eachEl in cups:
        newstring += str(eachEl.manufactuerDate) + ", "

    return HttpResponse('The manufacture dates of the cups are: ' + newstring)


def listnew(request):
    cups = Cup.objects.filter(manufactuerDate__gt='2012-01-01')
    newstring = ''
    for eachEl in cups:
        eachEl.material = 'slightly new'
        eachEl.save()
        newstring += eachEl.name + ", " + eachEl.material + ", " + str(eachEl.manufactuerDate) + ". "
    return HttpResponse(newstring)
