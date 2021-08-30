from .logic.logic_measurements import get_all_measurements
from .logic.logic_measurements import get_measurement_pk
from .logic.logic_measurements import delete_measurement_pk
from .logic.logic_measurements import change_unit_measurement_pk
from django.http import HttpResponse
from django.core import serializers

def get_measurements(request):
    measurements=get_all_measurements()
    measurement_list=serializers.serialize("json", measurements)
    return HttpResponse(measurement_list,content_type="application/json")
    

def get_measurement(request, pk):
    get_measurement=serializers.serialize("json", [get_measurement_pk(pk=pk)])
    return HttpResponse(get_measurement,content_type="application/json")
    
def delete_measurement(request, pk):
    delete_measurement_pk(pk=pk)
    measurement_list=serializers.serialize("json", get_all_measurements())
    return HttpResponse(measurement_list,content_type="application/json")
    
def change_measurement(request, pk, unit):
    measurement_change=serializers.serialize("json", [change_unit_measurement_pk(pk=pk, unit=unit)])
    return HttpResponse(measurement_change,content_type="application/json")
    