from django.test import TestCase 
import json
from rest_framework.test import APITestCase

from ..models import Worker

class TestWorkerList(APITestCase):
  def test_view_shound_be_assessible(self):
    respon = self.client.get('/workers/')
    # print(dir(respon))
    self.assertEqual(respon.status_code,200)
  def test_view_should_render_list_of_worker_names(self):
    #Given
    Worker.objects.create(
        first_name='first_name',
        last_name='last_name',
        is_available=True,
        primary_phone='09000000',
        secondary_phone='08000000',
        address='address',
      )
    Worker.objects.create(
        first_name='first_name2',
        last_name='last_name',
        is_available=True,
        primary_phone='09000000',
        secondary_phone='08000000',
        address='address',
      )

    exp = [  
          {"first_name": "first_name", 
          "last_name": "last_name", 
          "is_available": True, 
          "primary_phone": "09000000", 
          "secondary_phone": "08000000", 
          "address": "address"}, 
          
          {"first_name": "first_name2", 
          "last_name": "last_name", 
          "is_available": True, 
          "primary_phone": "09000000", 
          "secondary_phone": "08000000", 
          "address": "address"}
        ]  
    #When
    
    respon = self.client.get('/workers/')
 
    
    #Then
    # self.assertContains(respon,'<li>first_name</li>')
    # self.assertContains(respon,'<li>first_name2</li>')
    # self.assertEqual(respon.content.decode('utf-8') , json.dumps(exp) )
    self.assertEqual(respon.data ,exp)