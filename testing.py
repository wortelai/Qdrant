import requests

url = "https://j6yvgp8ptc.execute-api.us-west-2.amazonaws.com/Prod/hi" #sam-flask-app API gateway endpoint
# url = "http://35.91.179.112:8080/"  #(public IP address:port number) of EC2 instance on which flask app is running

response = requests.get(url=url)
print(response.text)