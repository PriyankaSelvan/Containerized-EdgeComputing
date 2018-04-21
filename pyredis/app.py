from bottle import redirect, template, request, response, route, run, get, post
import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.flushdb()
def main():
    run(host='0.0.0.0', port=8080)

BASE_TEMPLATE = """{{!data}}
        """        

@route('/')
def idx():
    data = """
    {{!data}}
    """
    the_template = template(BASE_TEMPLATE, data=data)

    inner_template = "{{key}} "

    keys = r.keys('*')

    data = ""
    for key in keys:
        data = data + template(inner_template, key=key)

    return template(the_template, data=data)

@post('/')
def create_new_key():
    key = request.POST.new_key
    val = request.POST.new_val
    r.set(key, val)
    redirect("/")
    
@get('/:key')
def the_get(key):
    the_template = template(BASE_TEMPLATE, data= """
    {{val}}
    """
    )
    return template(the_template, key=key, val=r.get(key))

@post('/:key')
def update_key(key):
    val = request.POST.new_val
    r.set(key, val)
    return template(BASE_TEMPLATE, data="" % (key, val))

main()
