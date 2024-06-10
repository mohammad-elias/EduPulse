from django.urls import path
from .views import InstitutionCreateView,StudentListCreateAPIView,SubjectListCreateAPIView

urlpatterns = [
    path('create/',InstitutionCreateView.as_view(),name='institute-create'),
    
    path('student-add/',StudentListCreateAPIView.as_view(),name='student-add'),
    
    path('subject/',SubjectListCreateAPIView.as_view(),name='subject-create'),
    
    # path('marks-add/std_id?<int:pk>/sub_id?<int:pk>/')
    

]
