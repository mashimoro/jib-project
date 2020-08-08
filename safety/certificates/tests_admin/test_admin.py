from django.test import TestCase
from ..models import Certificate
from ..admin import CertificateAdmin
# Create your tests here.

from django.contrib import admin
class CertificatesAdminTest(TestCase):
  def test_admin_shound_be_register(selt):
    #selt.assertTrue(isinstance(admin.site._registry[Certificate], CertificateAdmin))
    assert isinstance(admin.site._registry[Certificate], CertificateAdmin) is True

  def test_admin_shound_set_list_display(selt):
      experted = ('name', 'issued_by',)
      #selt.assertEqual(CertificateAdmin.list_display ,experted)
      assert CertificateAdmin.list_display == experted
