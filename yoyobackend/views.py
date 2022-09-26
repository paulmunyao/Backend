from django.shortcuts import render
import requests
# Create your views here.
r = requests.get('https://api.github.com/users/naveenkrnl')