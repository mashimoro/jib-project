from django.views import View
from django.http import HttpResponse
import requests
class Covid19ReportView(View):
  def get(self,request):
    r = requests.get('https://covid19.th-stat.com/api/open/today')
    data = r.json()
    newConfirmed = data['NewConfirmed']
    return HttpResponse(f'NewConfirmed: {newConfirmed}')
    #return HttpResponse()