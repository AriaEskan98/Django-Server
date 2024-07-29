from django.urls import path
from .views import import_data, list_records, get_record

urlpatterns = [
    path('import/', import_data, name='import_data'),
    path('detail/<str:model_name>/', list_records, name='list_records'),
    path('detail/<str:model_name>/<int:id>/', get_record, name='get_record'),
]
