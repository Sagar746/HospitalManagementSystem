# Generated by Django 3.2 on 2021-04-08 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField(default=0)),
                ('joining_date', models.DateField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField(default=0)),
                ('joining_date', models.DateField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField(default=0)),
                ('joining_date', models.DateField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=255)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Hospital.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_file', models.FileField(upload_to='')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('quantity', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=255)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('prescribed_by', models.ManyToManyField(to='Hospital.Doctor')),
                ('prescribed_to', models.ManyToManyField(to='Hospital.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='DoctorSalary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary_amount', models.PositiveIntegerField(default=0)),
                ('salary_date', models.DateField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Hospital.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False)),
                ('appointment_date', models.DateField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.patient')),
            ],
        ),
    ]
