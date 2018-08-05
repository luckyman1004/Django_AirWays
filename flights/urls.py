from django.urls import path

from .views import flights_list

urlpatterns = [
	path('flights/list/', flights_list, name='flights_list'),
]