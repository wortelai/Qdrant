import requests

url = "http://54.245.171.71:8080/"

response = requests.get(url=url)
print(response.text)