from django.test import TestCase
from ..serializers import CertificateModelSerializer
from ..models import Certificate

class TestCertificateModelSerializer(TestCase):
  def test_model_serializer_should_set_certificate(self):
    assert CertificateModelSerializer.Meta.model == Certificate

  def test_should_use_all_field(self):
    assert CertificateModelSerializer.Meta.fields == '__all__'