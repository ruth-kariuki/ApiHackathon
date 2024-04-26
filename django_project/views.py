import requests
from django.shortcuts import render

def home(request):
# USING APIS
  response = requests.get('https://randomfox.ca/floof/')
  data = response.json()
  results = data["image"]

  return render(request, 'templates/index.html', {'results': results})  
