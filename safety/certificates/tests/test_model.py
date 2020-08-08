from django.test import TestCase 
from ..models import Certificate

class TestCertificates(TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_certificates_should_defined_field(selt):
    name='Jad'
    issued_by='Put'
    cer = Certificate.objects.create(
    name=name,
    issued_by=issued_by,
    ) 
  
    assert cer.name == 'Jad'
    assert cer.issued_by == 'Put'
