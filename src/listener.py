import time
import datetime
import requests

url = "http://127.0.0.1:5000/get?key="

print("-"*10 + "Client Reading Keys" + "-"*10)

t_end = time.time() + 10
while t_end>time.time():
    data1 = requests.get(url+"key1")
    data1 = data1.json()
    print(datetime.datetime.now(), "Received key1 val:", data1['data'])
    data2 = requests.get(url+"key2").json()
    print(datetime.datetime.now(), "Received key2 val:", data2['data'])