import requests
from flask import Flask, json

def parseJson(data):
    parsed = list()
    parsed.append(f"{data['location'].get('name')}'s Weather Report")
    for key, value in data["current"].items():
            if key == "temp_f":
             parsed.append(f"The Current Temperature(f): {value}")
            if key == "is_day":
                if value == 1:
                    parsed.append(f"It is Currently Day time, and cloud coverage is at {data['current']['cloud']} %")
                else:
                    parsed.append(f"Nighttime is upon us and cloud coverage is at {data['current']['cloud']} %")
            if key == "wind_mph":
                parsed.append(f"Wind is currently at {value} mph.")
            if key == "humidity":
                parsed.append(f"{data['location'].get('name')}'s humidity is sitting at {value} %")       
    return parsed





















