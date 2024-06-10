from django.urls import path,include
from rest_framework import routers
from .views import FeatureViewset,PlanViewset


router = routers.DefaultRouter()
router.register(r'features', FeatureViewset,basename='feature')
router.register(r'plan', PlanViewset,basename='plan')


urlpatterns = [
    path('',include(router.urls)),
]



