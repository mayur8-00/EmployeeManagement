from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.employee_list,
        name="employee_list"
    ),

    path(
        "employee/add/",
        views.employee_create,
        name="employee_create"
    ),

    path(
        "employee/<int:id>/",
        views.employee_detail,
        name="employee_detail"
    ),

    path(
        "employee/<int:id>/edit/",
        views.employee_update,
        name="employee_update"
    ),

    path(
        "employee/<int:id>/delete/",
        views.employee_delete,
        name="employee_delete"
    ),
]