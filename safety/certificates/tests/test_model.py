from django.test import TestCase 
from ..models import Certificate
from workers.models import Worker
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
            primary_phone='primary_phone',
            secondary_phone='secondary_phone',
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
