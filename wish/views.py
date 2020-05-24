from django.shortcuts import render
from .models import wishlist

# Create your views here.

def home(request):
	wishes = wishlist.objects.order_by('-id')[0]
	return render(request, 'wish/home.html', {'wishes':wishes})