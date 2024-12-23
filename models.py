from django.db import models
from django.utils import timezone


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)  # Optional

    def __str__(self):
        return f"{self.first_name}"

class Club(models.Model):
    club_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)  # Optional

    def __str__(self):
        return f"{self.club_name}"

class Membership(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    join_date = models.DateField(auto_now_add=True)
    role = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.student}"



