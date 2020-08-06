from django.test import TestCase
from ..models import Worker
from ..admin import WorkerAdmin 
 
# Create your tests here.
 
from django.contrib import admin
class WorkAdminTest(TestCase):
  def test_admin_shound_be_register(selt):
      selt.assertTrue(isinstance(admin.site._registry[Worker],WorkerAdmin))

  def test_admin_shound_set_list_display(selt):
      experted = (
      'first_name','last_name',
      )
      selt.assertEqual(WorkerAdmin.list_display ,experted)

  def test_admin_shound_set_list_filter(selt):
    experted = ( 'is_available',)
    selt.assertEqual(WorkerAdmin.list_filter ,experted)