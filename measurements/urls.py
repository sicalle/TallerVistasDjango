from django.urls import path 
from . import views 

urlpatterns= [
    path('list/', views.get_measurements, name='measurement_list'),
    path('search/<int:pk>/', views.get_measurement, name='get_measurement_pk'),
    path('delete/<int:pk>/', views.delete_measurement, name='delete_measurement_pk'),
    path('change/<int:pk>/<str:unit>', views.change_measurement, name='change_measurement_pk')
]
