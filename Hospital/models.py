from django.db import models

# Create your models here.

class Doctor(models.Model):
	first_name=models.CharField(max_length=255)
	last_name=models.CharField(max_length=255)
	phone=models.CharField(max_length=255)
	address=models.CharField(max_length=255)
	age=models.PositiveIntegerField(default=0)
	joining_date=models.DateField()
	added_on=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.first_name + ' ' + self.last_name

class Patient(models.Model):
	first_name=models.CharField(max_length=255)
	last_name=models.CharField(max_length=255)
	phone=models.CharField(max_length=255)
	address=models.CharField(max_length=255)
	age=models.PositiveIntegerField(default=0)
	joining_date=models.DateField()
	added_on=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.first_name + ' ' + self.last_name


class Medicine(models.Model):
	name=models.CharField(max_length=255)
	prescribed_by=models.ManyToManyField(Doctor)
	prescribed_to=models.ManyToManyField(Patient)
	quantity=models.IntegerField(default=0)
	description=models.CharField(max_length=255)
	added_on=models.DateTimeField(auto_now_add=True)

class Appointment(models.Model):
	patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
	doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
	approved=models.BooleanField(default=False)
	appointment_date=models.DateField()
	added_on=models.DateTimeField(auto_now_add=True)

class Report(models.Model):
	patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
	doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
	report_file=models.FileField()
	added_on=models.DateTimeField(auto_now_add=True)

class Speciality(models.Model):
	doctor=models.OneToOneField(Doctor,on_delete=models.CASCADE)
	field=models.CharField(max_length=255)
	added_on=models.DateTimeField(auto_now_add=True)

class Nurse(models.Model):
	first_name=models.CharField(max_length=255)
	last_name=models.CharField(max_length=255)
	phone=models.CharField(max_length=255)
	address=models.CharField(max_length=255)
	age=models.PositiveIntegerField(default=0)
	joining_date=models.DateField()
	added_on=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.first_name + ' ' + self.last_name



class DoctorSalary(models.Model):
	doctor=models.OneToOneField(Doctor,on_delete=models.CASCADE)
	salary_amount=models.PositiveIntegerField(default=0)
	salary_date=models.DateField()
	added_on=models.DateTimeField(auto_now_add=True)

class Admin(models.Model):
	first_name=models.CharField(max_length=255)
	last_name=models.CharField(max_length=255)
	email=models.EmailField()
	password=models.CharField(max_length=255)

	def __str__(self):
		return self.first_name + ' ' + self.last_name
