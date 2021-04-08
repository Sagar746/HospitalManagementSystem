from django.contrib import admin
from .models import Doctor,Patient,Medicine,Appointment,Report,Speciality,Nurse,DoctorSalary,Admin

# Register your models here.

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Medicine)
admin.site.register(Appointment)
admin.site.register(Report)
admin.site.register(Speciality)
admin.site.register(Nurse)
admin.site.register(DoctorSalary)
admin.site.register(Admin)