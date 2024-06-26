# Generated by Django 5.0.1 on 2024-06-09 19:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('roll', models.IntegerField()),
                ('total_marks', models.FloatField(default=0)),
                ('average_marks', models.FloatField(default=0)),
                ('gpa', models.CharField(default='Undefine', max_length=10)),
                ('stud_institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_records', to='management.institution')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=100)),
                ('sub_marks', models.IntegerField()),
                ('subject_institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_records', to='management.institution')),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obtain_marks', models.FloatField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marks', to='institute.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marks', to='institute.subject')),
            ],
            options={
                'unique_together': {('student', 'subject')},
            },
        ),
    ]
