import requests


for i in range(0, 10):
    response = requests.get('http://localhost:8888')
    print(response.text)