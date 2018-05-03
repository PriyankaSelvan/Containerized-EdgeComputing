from bottle import redirect, template, request, response, route, run, get, post
import requests
import random

redisqueue = open('numberserver/server', 'r').readlines()[0].strip()

def main():
    run(host='0.0.0.0', port=8010)

BASE_TEMPLATE = """{{!data}}
        """        


@post('/')
def create_new_key():
    line = request.POST.new_key
    rn = '_' + str(random.randint(0, 100))
    day, time, sensor, state = line.split(' ')
    val = state + ' ' + time
    k = sensor + rn
    data = {'new_key':k, 'new_val':val}
    r = requests.post(url = redisqueue, data = data)
    redirect("/")
    
@get('/:key')
def the_get(key):
    the_template = template(BASE_TEMPLATE, data= """
    {{val}}
    """
    )
    url = redisqueue + str(key)
    get = requests.get(url=url) 
    return template(the_template, val=get.text.strip())

main()
