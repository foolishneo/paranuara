from django.urls import path
from . import views

urlpatterns = [    
    path('', views.index, name='index'),
    path(
        'api/v1/company/<int:company_id>/',
        views.get_company_employees,
        name="get company's employees"
    ),
    path(
        'api/v1/person/<int:id1>/<int:id2>/',
        views.get_people_common_friends,
        name='get people info and common friends'
    ),
    path(
        'api/v1/person/<int:id>/food/',
        views.get_person_favourite_food,
        name='get person favourite fruits and vegetables'
    ),
]