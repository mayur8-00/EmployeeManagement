from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import Employee
from .models import Department

# ==========================================
# HOME / EMPLOYEE LIST
# ==========================================

def employee_list(request):

    search = request.GET.get(
        "search",
        ""
    ).strip()


    employees = Employee.objects.select_related(
        "department"
    ).all().order_by("-id")


    if search:

        employees = employees.filter(

            name__icontains=search

        ) | employees.filter(

            email__icontains=search

        ) | employees.filter(

            phone__icontains=search

        ) | employees.filter(

            position__icontains=search

        ) | employees.filter(

            department__name__icontains=search
        )


    total_employees = Employee.objects.count()

    total_departments = Department.objects.count()


    context = {

        "employees": employees,

        "search": search,

        "total_employees": total_employees,

        "total_departments": total_departments,
    }


    return render(

        request,

        "employees/employee_list.html",

        context
    )


# ==========================================
# EMPLOYEE DETAIL
# ==========================================

def employee_detail(request, id):

    employee = get_object_or_404(

        Employee.objects.select_related(
            "department"
        ),

        id=id
    )

    return render(

        request,

        "employees/employee_detail.html",

        {
            "employee": employee
        }
    )

# ==========================================
# ADD EMPLOYEE
# ==========================================
def employee_create(request):

    departments = Department.objects.all().order_by("name")

    if request.method == "POST":

        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        gender = request.POST.get("gender", "")
        department_id = request.POST.get("department", "")
        position = request.POST.get("position", "").strip()
        salary = request.POST.get("salary", "")
        joining_date = request.POST.get("joining_date", "")
        address = request.POST.get("address", "").strip()

        # Get Department object using ID
        department = get_object_or_404(
            Department,
            id=department_id
        )

        # Create Employee
        Employee.objects.create(

            name=name,

            email=email,

            phone=phone,

            gender=gender,

            department=department,

            position=position,

            salary=salary,

            joining_date=joining_date,

            address=address,
        )

        return redirect("employee_list")

    context = {

        "departments": departments,

        "title": "Add Employee",

        "button_text": "Add Employee",
    }

    return render(
        request,
        "employees/employee_form.html",
        context
    )

# ==========================================
# UPDATE EMPLOYEE
# ==========================================

def employee_update(request, id):

    employee = get_object_or_404(

        Employee,

        id=id
    )

    departments = Department.objects.all().order_by(
        "name"
    )

    if request.method == "POST":

        employee.name = request.POST.get(
            "name"
        ).strip()


        employee.email = request.POST.get(
            "email"
        ).strip()


        employee.phone = request.POST.get(
            "phone"
        ).strip()


        employee.gender = request.POST.get(
            "gender"
        )

        employee.department_id = request.POST.get(
            "department"
        )


        employee.position = request.POST.get(
            "position"
        ).strip()


        employee.salary = request.POST.get(
            "salary"
        )

        employee.joining_date = request.POST.get(
            "joining_date"
        )


        employee.address = request.POST.get(
            "address"
        ).strip()


        employee.save()


        return redirect(

            "employee_detail",

            id=employee.id
        )


    context = {

        "employee": employee,

        "departments": departments,

        "title": "Update Employee",

        "button_text": "Update Employee",
    }

    return render(

        request,

        "employees/employee_form.html",

        context
    )

# ==========================================
# DELETE EMPLOYEE
# ==========================================

def employee_delete(request, id):

    employee = get_object_or_404(

        Employee,

        id=id
    )


    if request.method == "POST":

        employee.delete()


        return redirect(
            "employee_list"
        )


    return render(

        request,

        "employees/employee_confirm_delete.html",

        {
            "employee": employee
        }
    )