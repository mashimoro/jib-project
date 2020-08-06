from django.contrib import admin
from .models import Worker
# Register your models here.

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
  list_display = (
    'first_name', 
    'last_name',
  )
  list_filter = (
      'is_available',
  )