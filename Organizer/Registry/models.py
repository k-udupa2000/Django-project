from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import RegexValidator

class Student(models.Model):
    
    studentName = models.CharField(max_length=250, default = "", verbose_name = "Student Name")
    phone1_regex = RegexValidator(regex = r'^[0-9]{10}$', message = "Phone number must be of the form: 9876543210.")
    phone1 = models.CharField(validators = [phone1_regex], max_length = 11, verbose_name = "Primary Phone No.")
    phone2 = models.CharField(validators = [phone1_regex], max_length = 11, verbose_name = "Secondary Phone No.", blank = True)

    lastFeesPaid = models.DateTimeField(verbose_name = "Last fees paid")

    lastAttended = models.DateTimeField(verbose_name = "Last class attended")

    def __str__(self):
        return self.studentName

'''
class Users(models.Model):

    username = models.CharField(max_length=250, default = "", verbose_name = "User Name")
    password = models.CharField(max_length=100, default="",verbose_name = "Password")

    def __str__(self):
        return self.username
'''