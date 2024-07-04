import requests
from flask import Flask, json


apikey = "59983720c6894ce7ae5193852240107"
inputloc = input("Enter city here ")
response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={apikey}&q={inputloc}")
data = response.json()
# print(type(data), data)
for key, value in data.items():
    print(key, type(value))
    for k, v in value.items():
        print(k, v)

    









