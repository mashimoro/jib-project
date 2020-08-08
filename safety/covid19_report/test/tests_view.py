from django.test import TestCase
from unittest.mock import patch

# from v
# Create your tests here.
class TestCovid19ReportView(TestCase):
  def test_view_should_be_accesible(self):
    response = self.client.get('/covid19-reports/')
    self.assertEqual(response.status_code,200)

  @patch('covid19_report.views.requests.get')
  def test_view_shound_call_covidApi(self,mock):
    self.client.get('/covid19-reports/')
    mock.assert_called_once_with('https://covid19.th-stat.com/api/open/today')
    # response = self.client.get('/covid19-reports/')
    # print(f'response=={response}')

