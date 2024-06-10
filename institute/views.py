from rest_framework import generics
from management.models import Institution
from .models import Student,Subject,Marks
from .serializers import InstitutionSerializer,StudentSerializer,SubjectSerializer,MarksSerializer
from .permissions import IsAdminUser
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated


class InstitutionCreateView(generics.CreateAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    permission_classes = [IsAuthenticated,IsAdminUser]

    def perform_create(self, serializer):
        user = self.request.user

        if Institution.objects.filter(created_by=user).exists():
            raise ValidationError("You have already created an institution.")

        if user.plan == 'basic':
            students = 100  
        elif user.plan == 'premium':
            students = 500  
        else:
            students = 0  

        institution = serializer.save(created_by=user, students=students)

        user.institutions = institution
        user.save()
    

class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated,IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(stud_institution=self.request.user.institutions)
     
        
class SubjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated,IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(subject_institution=self.request.user.institutions)
        
        
class SubjectListCreateAPIView(generics.ListCreateAPIView):
    queryset=Marks.objects.all()
    serializer_class = MarksSerializer
    permission_classes = [IsAuthenticated,IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(subject_institution=self.request.user.institutions)
