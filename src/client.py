import time
import datetime
import requests

url = "http://127.0.0.1:5000/post"

print("-"*10 + "Client Sending Load" + "-"*10)

t_end = time.time() + 12
counter = 0
while t_end>time.time():
    value1 = 'value'+str(counter)
    data1 = {'key':'key1','value':value1}
    result = requests.post(url,json=data1).json()
    print(datetime.datetime.now(), "Posting " + value1 + " on key1:", result['status'])
    counter += 1
    value2 = 'value'+str(counter)
    data2 = {'key':'key2','value':value2}
    result = requests.post(url,json=data2).json()
    print(datetime.datetime.now(), "Posting " + value2 + " on key2:", result['status'])
    counter += 1