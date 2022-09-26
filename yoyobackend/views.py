# from django.shortcuts import render
import requests
# Create your views here.
response = requests.get('https://api.github.com/users/naveenkrnl')

print(r)
print(r.content)