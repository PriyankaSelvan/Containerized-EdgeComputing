import requests
from datetime import datetime
def subtract(a, b):
    return str(datetime.strptime(a, '%H:%M:%S.%f') - datetime.strptime(b, '%H:%M:%S.%f'))



urlall = "http://18.204.216.188:8000/"
storage = {}

while True:
    getall = requests.get(url = urlall)

    keys = getall.text.strip().split()
    if len(keys) > 0:
        for key in keys:
            if len(key.split('_')) == 2:
                sensor = key.split('_')[0]
                urlkey = urlall + key
                get = requests.get(url=urlkey)
                val = get.text.strip()
                if len(val.split(' ')) == 2:
                    state, time = val.split(' ')
                    if state == 'true':
                        storage[sensor] = time
                    elif state == 'false':
                        toput = subtract(time, storage[sensor])
                        storage.pop(sensor, None)
                        data2 = {'new_val':toput}
                        url2 = urlall + sensor
                        r = requests.post(url = url2, data = data2)
                    data1 = {'new_val':'random'}
                    url1 = urlall + key
                    r = requests.post(url = url1, data = data1)

