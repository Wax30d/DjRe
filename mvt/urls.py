from django.urls import path
from . import views

urlpatterns = [
    path('mvt/', views.mvt),

    path('people/', views.person_list, name='person_list'),
    path('people/<pk>/', views.person_detail, name='person_detail'),
    path('passport/', views.passport_list, name='passport_list'),
    path('passport/<pk>/', views.passport_detail, name='passport_detail'),

    path('reporters/', views.reporter_list, name='reporter_list'),
    path('reporters/<pk>/', views.reporter_detail, name='reporter_detail'),
    path('articles/', views.article_list, name='article_list'),
    path('articles/<pk>/', views.article_detail, name='article_detail'),

    path('carmodel/', views.carmodel_list, name='carmodel_list'),
    path('carmodel/<pk>/', views.carmodel_detail, name='carmodel_detail'),
    path('fuel_type/', views.fuel_type_list, name='fuel_type_list'),
    path('fuel_type/<pk>/', views.fuel_type_detail, name='fuel_type_detail'),
]
