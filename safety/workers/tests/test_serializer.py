from django.test import TestCase 
from ..serializers import WorkerSerializer
from ..models import Worker
import os
from django.core.files import File
from unittest.mock import MagicMock

class TestWorkerSerializer(TestCase):
  def test_serializer_should_return_field_worker_serializer_data(selt):
      first_name='Jad1'
      last_name='Put'
      is_available=True
      primary_phone='0123456789'
      secondary_phone='0123456789'
      address='Geek Bass All Star' 
     
      worker = Worker.objects.create(
        first_name=first_name,
        last_name=last_name,
        is_available=is_available,
        primary_phone=primary_phone,
        secondary_phone=secondary_phone,
        address=address,
      )
      serialized = WorkerSerializer(worker)
      # print(f'serialized : {serialized}')
      expc = {
          'first_name':'Jad1',
          'last_name':'Put',
          'is_available':True,
          'primary_phone':'0123456789',
          'secondary_phone':'0123456789',
          'address':'Geek Bass All Star',
          }
  # print(f'{expc} : serialized : {serialized}')

      assert serialized.data == expc
      qr_mock = MagicMock(spec=File)
      qr_mock.name = f'qr_code-{first_name}.png'
      os.remove(f'media/qr_code/{qr_mock.name}')