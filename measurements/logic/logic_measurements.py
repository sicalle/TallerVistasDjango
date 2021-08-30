from ..models import Measurement

def get_all_measurements():
    measurements=Measurement.objects.all()    
    return measurements

def get_measurement_pk(pk):
    measurement=Measurement.objects.get(id=pk)   
    return measurement

def delete_measurement_pk(pk):
    Measurement.objects.filter(id = pk).delete()
   
def change_unit_measurement_pk(pk, unit):
    measurement=Measurement.objects.get(id=pk) 
    measurement.unit= unit
    measurement.save()
    return measurement

