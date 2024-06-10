from django.db import models
from management.models import Institution

class Student(models.Model):
    name = models.CharField(max_length=200)
    roll = models.IntegerField()
    total_marks = models.FloatField(default=0)
    average_marks = models.FloatField(default=0)
    gpa = models.CharField(max_length=10, default='Undefine')
    stud_institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name='student_records')

    def __str__(self):
        return self.name
    
class Subject(models.Model):
    sub_name = models.CharField(max_length=100)
    sub_marks = models.IntegerField()
    subject_institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name='subject_records')

    def __str__(self):
        return self.sub_name

class Marks(models.Model):
    obtain_marks = models.FloatField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='marks')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='marks')

    class Meta:
        unique_together = ['student', 'subject']

    def __str__(self):
        return f"Marks: {self.obtain_marks}, Student: {self.student}, Subject: {self.subject}"
