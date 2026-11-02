from django.db import models
class Department(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    description = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.name

class Employee(models.Model):

    GENDER_CHOICES = [

        ("Male", "Male"),

        ("Female", "Female"),

        ("Other", "Other"),
    ]

    name = models.CharField(
        max_length=100
    )

    email = models.EmailField(
        unique=True
    )

    phone = models.CharField(
        max_length=15
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    department = models.ForeignKey(

        Department,

        on_delete=models.CASCADE,

        related_name="employees"
    )

    position = models.CharField(
        max_length=100
    )

    salary = models.DecimalField(

        max_digits=10,

        decimal_places=2
    )

    joining_date = models.DateField()
    address = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):

        return self.name