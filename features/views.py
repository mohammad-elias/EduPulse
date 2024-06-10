from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FeatureSerializer,PlanSerializer
from .models import Feature,Plan
from .permissions import IsAdminOrReadOnly

# Create your views here.
class FeatureViewset(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    permission_classes = [IsAdminOrReadOnly]


class PlanViewset(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [IsAdminOrReadOnly]