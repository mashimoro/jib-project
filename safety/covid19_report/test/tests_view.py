from django.test import TestCase
from unittest.mock import patch

# from v
# Create your tests here.
#stap ไม่ให้ test นี้ออก api จริง

class TestCovid19ReportView(TestCase):
  @patch('covid19_report.views.requests.get')
  def test_view_should_be_accesible(self,_):
    response = self.client.get('/covid19-reports/')
    self.assertEqual(response.status_code,200)

  @patch('covid19_report.views.requests.get')
  def test_view_should_call_covidApi(self,mock):
    self.client.get('/covid19-reports/')
    mock.assert_called_once_with('https://covid19.th-stat.com/api/open/today')
    # response = self.client.get('/covid19-reports/')
    # print(f'response=={response}')
  @patch('covid19_report.views.requests.get') 
  def test_view_should_render_confirmed(self,mock):
    r = mock.return_value
    r.json.return_value = {
            "Confirmed": 3345,
            "Recovered": 3148,
            "Hospitalized": 139,
            "Deaths": 58,
            "NewConfirmed": 50,
            "NewRecovered": 0,
            "NewHospitalized": 15,
            "NewDeaths": 0,
            "UpdateDate": "07/08/2020 11:36",
            "Source": "https://covid19.th-stat.com/",
            "DevBy": "https://www.kidkarnmai.com/",
            "SeverBy": "https://smilehost.asia/"
        }
    response = self.client.get('/covid19-reports/')
    self.assertContains(response ,'NewConfirmed: 50')


