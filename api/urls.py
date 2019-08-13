from django.urls import path
from . import views

urlpatterns = [    
    path(
        'api/v1/company/<int:company_id>/',
        views.get_employees_by_company_id,
        name='get employees by company id'
    ),
    path(
        'api/v1/person/<int:id1>/<int:id2>/',
        views.get_people_by_id,
        name='get people by id'
    ),
    path(
        'api/v1/person/<int:id>/food/',
        views.get_person_food,
        name='get person favourite fruits and vegetables'
    ),
]