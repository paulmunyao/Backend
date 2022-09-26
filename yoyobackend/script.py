import requests
# Create your views here.
response = requests.get('https://api.github.com/users/naveenkrnl')

print(response.url)

print(response.status_code)