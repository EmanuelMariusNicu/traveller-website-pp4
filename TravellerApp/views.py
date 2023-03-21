from django.shortcuts import render
from django.views import generic
from .models import Trip
# Create your views here.

class TripList(generic.ListView):
    model = Trip
    queryset = Trip.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6
