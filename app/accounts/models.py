from django.db import models
from django.contrib.auth.models import User,auth
from django.conf import settings


class Department(models.Model):
    dept_name=models.AutoField(primary_key=True)
    building=models.CharField(max_length=50)
    budget=models.CharField(max_length=50)
    #c= models.ForeignKey(Company, default=1,on_delete=models.SET_DEFAULT)
    #d= models.ForeignKey(Branch, default=1, on_delete=models.SET_DEFAULT)
    #b= models.ForeignKey(Department, default=1, on_delete=models.SET_DEFAULT)
    class Meta:
        db_table="department"

class Course(models.Model):
    course_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    credits=models.CharField(max_length=50)
    dept_name= models.ForeignKey(Department, default=1,on_delete=models.SET_DEFAULT)
    #d= models.ForeignKey(Branch, default=1, on_delete=models.SET_DEFAULT)
    #b= models.ForeignKey(Department, default=1, on_delete=models.SET_DEFAULT)
    class Meta:
        db_table="course"

class Student(models.Model):
    student_id=models.AutoField(primary_key=True)
    user_id= models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.SET_DEFAULT)
    #b= models.ForeignKey(Department, default=1, on_delete=models.SET_DEFAULT)
    class Meta:
        db_table="student"
