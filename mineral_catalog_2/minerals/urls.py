from django.urls import path

from . import views


app_name = 'minerals'
urlpatterns = [
    path('', views.mineral_list, name='list'),
    path('details/<pk>/', views.mineral_details, name='details'),
    path('search/<letter>/', views.mineral_by_letter, name='by_letter'),
    path('search/', views.search_term, name='search'),
    path('<group>/', views.group_search, name='group')
]