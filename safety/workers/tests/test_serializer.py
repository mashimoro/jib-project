from django.test import TestCase 
from ..serializers import WorkerSerializer
from ..models import Worker


class TestWorkerSerializer(TestCase):
  def test_serializer_should_return_field_worker_serializer_data(selt):
      first_name='Jad'
      last_name='Put'
      is_available=True
      primary_phone='089-888-xxxx'
      secondary_phone='089-333-4444'
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
      expc = {
          'first_name':'Jad',
          'last_name':'Put',
          'is_available':True,
          'primary_phone':'089-888-xxxx',
          'secondary_phone':'089-333-4444',
          'address':'Geek Bass All Star',
          }
      assert serialized.data == expc