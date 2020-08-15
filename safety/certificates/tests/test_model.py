from django.test import TestCase 
from ..models import Certificate
from workers.models import Worker
import os
class TestCertificates(TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_certificates_should_defined_field(selt):

    worker = Worker.objects.create(
            first_name='first_name',
            last_name='last_name',
            is_available=True,
            primary_phone='0123456789',
            secondary_phone='0123456789',
            address='address' 
          )

    name='Jad'
    issued_by='Put'
    certificate = Certificate.objects.create(
    name=name,
    issued_by=issued_by,
    worker=worker,
    ) 
  
    assert certificate.name == 'Jad'
    assert certificate.issued_by == 'Put'
    assert certificate.worker.first_name == 'first_name'
    os.remove(f'media/qr_code/qr_code-first_name.png') 
