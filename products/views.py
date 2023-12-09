from django.shortcuts import render
from .models import Product ,Brand , Review
from django.views.generic import ListView ,DetailView
# Create your views here.

class ProductList(ListView):
    model = Product


class ProductDetail(DetailView):
    model = Product