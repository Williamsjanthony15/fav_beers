from django.shortcuts import render
from .models import Beer
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
# Create your views here.

class BeerList(ListView):
    template_name = 'beerList.html'
    model = Beer
    
class BeerAdd(CreateView):
    template_name = 'beerAdd.html'
    model = Beer
    fields = ['title', 'description', 'userName' ]
    
class BeerDetails(DetailView):
    template_name = 'beerDetails.html'
    model = Beer

class BeerUpdate(UpdateView):
    template_name = 'beerUpdate.html'
    model = Beer
    fields = ['title', 'description', 'userName' ]

class BeerDelete(DeleteView):
    template_name = 'beerDelete.html'
    model = Beer
    success_url = reverse_lazy('lists')
