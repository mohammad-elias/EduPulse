from rest_framework import viewsets
from .models import Contact
from .serializers import ContactSerializer
from .permissions import CanViewMessages


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [CanViewMessages]
