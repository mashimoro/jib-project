import os
from django.test import TestCase
from django.core.files import File
from ..models import Worker
from unittest.mock import MagicMock

class TestWorker(TestCase):
  def test_worker_should_defined_field(selt):
        #Given
        first_name='Jad'
        last_name='Put'
        is_available=True
        primary_phone='0123456789'
        secondary_phone='0123456789'
        address='Geek Bass All Star' 
        
        image_mock = MagicMock(spec=File)
        image_mock.name = 'Jad_image'
        qr_mock = MagicMock(spec=File)
        qr_mock.name = f'qr_code-{first_name}.png'
        

        #When
        worker = Worker.objects.create(
            first_name=first_name,
            last_name=last_name,
            is_available=is_available,
            primary_phone=primary_phone,
            secondary_phone=secondary_phone,
            address=address,
            image_profile=image_mock,
            qr_code=qr_mock,
          )
        #Then
        # selt.assertEqual(worker.first_name,first_name)
        #selt.assertEquals(worker.image_profile.name, 'Jad_image')
        assert worker.image_profile.name == 'Jad_image'
        assert worker.is_available == True
        print(f'qr_code :#######{worker.qr_code}')
        assert  worker.qr_code == f'qr_code/{qr_mock.name}'
        os.remove('media/Jad_image')
        os.remove(f'media/qr_code/{qr_mock.name}')


  def test_model_should_have_fname(self):
    first_name ='first_nameXX'
    last_name = 'last_name'
    qr_mock = MagicMock(spec=File)
    qr_mock.name = f'qr_code-{first_name}.png'

    worker = Worker.objects.create(
            first_name='first_nameXX',
            last_name='last_name',
            is_available=True,
            primary_phone='0123456789',
            secondary_phone='0123456789',
            address='address' 
          )
    assert worker.__str__() == f'{first_name} {last_name}'
    os.remove(f'media/qr_code/{qr_mock.name}')
