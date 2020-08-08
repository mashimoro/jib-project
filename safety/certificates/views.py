from django.shortcuts import render
from .serializers  import CertificateModelSerializer
from rest_framework.viewsets import ModelViewSet

from .models import Certificate
# Create your views here.

class CertificateModelViewSetView(ModelViewSet):
  queryset = Certificate.objects.all()
  serializer_class = CertificateModelSerializer