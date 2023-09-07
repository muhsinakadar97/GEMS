from django.db import models


# Create your models here.
class Enquiry(models.Model):
    name = models.CharField(max_length=250)
    address = models.TextField()
    contact = models.IntegerField()
    course = models.TextField()

    def __str__(self):
        return self.name
class Admission(models.Model):
    gemid=models.IntegerField()
    stud_name=models.CharField(max_length=250)
    parent_name=models.CharField(max_length=250)
    parent_contact=models.IntegerField()
    stud_address=models.TextField()
    stud_contact=models.IntegerField()
    qualification=models.CharField(max_length=250)
    dob=models.DateField()
    gender=models.CharField(max_length=250)
    course1=models.CharField(max_length=250)
    course2=models.CharField(max_length=250)
    course3=models.CharField(max_length=250)
    course_duration=models.IntegerField()
    scheme=models.CharField(max_length=250)
    fee=models.IntegerField()
    joining_date=models.DateField()
    exam_date=models.DateField()
    certificate_status=models.CharField(max_length=250)

    def __str__(self):
        return self.stud_name
