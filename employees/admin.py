from django.contrib import admin
from .models import Department
from .models import Employee

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "description",
        "created_at",
    )

    search_fields = (
        "name",
    )

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    list_display = (

        "id",

        "name",

        "email",

        "phone",

        "gender",

        "department",

        "position",

        "salary",

        "joining_date",
    )

    search_fields = (

        "name",

        "email",

        "phone",

        "position",
    )

    list_filter = (

        "gender",

        "department",

        "joining_date",
    )

    ordering = (
        "-id",
    )