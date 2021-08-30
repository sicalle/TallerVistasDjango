from .logic.logic_variables import get_all_variables
from django.http import HttpResponse
from django.core import serializers

def get_variables(request):
    variables=get_all_variables()
    variable_list=serializers.serialize("json", variables)
    return HttpResponse(variable_list,content_type="application/json")
    