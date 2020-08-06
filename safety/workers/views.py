from django.views import View
from django.http import HttpResponse
from django.shortcuts import render
import json

from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.views import APIView

from .models import Worker


class WorkerSerializer(serializers.Serializer):
    first_name=serializers.CharField(max_length=30)
    last_name=serializers.CharField(max_length=40)
    is_available=serializers.BooleanField()
    primary_phone=serializers.CharField(max_length=10)
    secondary_phone=serializers.CharField(max_length=10)
    address=serializers.CharField()
class WorkerListView(APIView):
  def get(self, request):
    workers = Worker.objects.all()
    serializer = WorkerSerializer( workers,many= True)
    return Response(serializer.data)
    # html =''
    # for worker in workers:
    #   html += f'<li>{worker.first_name}</li>'
    # return HttpResponse(html)
    # worker_list = []
    # for worker in workers:
    #   dt = {
    #     'first_name' : worker.first_name,
    #     'last_name' :worker.last_name,
    #     'is_available' :worker.is_available,
    #     'primary_phone' : worker.primary_phone,
    #     'secondary_phone' : worker.secondary_phone,
    #     'address' : worker.address,
    #   }
    #   worker_list.append(dt) 
    # return HttpResponse(json.dumps(worker_list), content_type='application/json')
    # 
    # return render(request,'worker_list.html',{'workers' : worker_list})

