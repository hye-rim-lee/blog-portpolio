from django.shortcuts import render
from .models import Portfolio

# Create your views here.

def portfolio(request):
    portfolio = portfolios.objects
    return render(request, 'portfolio.html', {'portfolios' : portfolios})