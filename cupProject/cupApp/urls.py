from django.urls import path
from . import views

# paths that trigger functions in views file
urlpatterns = [
    path('', views.index, name='index'),

    path('hello/<str:name>/', views.greeting, name='ex1a'),
    path('timestwo/<int:number>/', views.multiply, name='ex1b'),
    path('total/<int:mytotal>/', views.add, name='ex1c'),

    path('addCup1', views.addcup1, name='ex2a'),
    path('addCup2', views.addcup2, name='ex2b'),

    path('all/', views.all, name='ex2c'),

    path('listnew', views.listnew, name='ex2d'),

    path('cupindex', views.cupindex, name='ex3'),
]
