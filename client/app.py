import requests
import random
import time

URL = "http://54.82.255.37:8001/"
sensors = set()
for line in open('short_data.txt', 'r'):
    #rn = random.randint(0, 100)
    key = line.strip()
    data = {'new_key':key}
    r = requests.post(url = URL, data = data)
    time.sleep(2)
    sensors.add(key.split(' ')[2])

for key in sensors:
    r = requests.get(url = URL+key)
    print("From server value for key ", key , " is ", r.text)
