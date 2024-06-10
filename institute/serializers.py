from rest_framework import serializers
from management.models import Institution
from .models import Student,Subject,Marks
from django.contrib.auth import get_user_model

User = get_user_model()

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ['id', 'name', 'address', 'logo', 'phone',' students']
        read_only_fields = ['students']

    def create(self, validated_data):
        return Institution.objects.create(**validated_data)
    
    
    
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'total_marks', 'average_marks', 'gpa']
        read_only_fields = ['total_marks', 'average_marks', 'gpa']

    # def validate(self, data):
    #     total_marks = data.get('total_marks')
    #     num_subjects = data.get('subject_records').count() 
    #     subject_records = data.get('subject_records')
    #     print(subject_records)
    #     num_subjects = Subject.objects.filter(subject_institution=3).count()
    #     print(num_subjects)
    #     if num_subjects == 0:
    #         raise serializers.ValidationError("No subjects provided for the student.")
         
    #     data['average_marks'] = total_marks / num_subjects if num_subjects else 0
        
        
    #     if data['average_marks'] >= 90:
    #         data['gpa'] = 'A+'
    #     elif data['average_marks'] >= 80:
    #         data['gpa'] = 'A'
    #     elif data['average_marks'] >= 70:
    #         data['gpa'] = 'B+'
    #     elif data['average_marks'] >= 60:
    #         data['gpa'] = 'B'
    #     else:
    #         data['gpa'] = 'Fail'

    #     return data

        
        
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'sub_name', 'sub_marks']
        

class MarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marks
        fields = ['id', 'obtain_marks', 'student','subject']
        read_only_fields = ['student','subject']