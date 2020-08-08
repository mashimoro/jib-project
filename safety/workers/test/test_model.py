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
        primary_phone='089-888-xxxx'
        secondary_phone='089-333-4444'
        address='Geek Bass All Star' 
        
        image_mock = MagicMock(spec=File)
        image_mock.name = 'Jad_image'

        #When
        worker = Worker.objects.create(
            first_name=first_name,
            last_name=last_name,
            is_available=is_available,
            primary_phone=primary_phone,
            secondary_phone=secondary_phone,
            address=address,
            image_profile=image_mock,
          )
        #Then
        selt.assertEqual(worker.first_name,first_name)
        selt.assertEquals(worker.image_profile.name, 'Jad_image')
        os.remove('media/Jad_image')