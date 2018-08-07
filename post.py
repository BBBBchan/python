import urllib2
import json

def post():
    url = "http://127.0.0.1:5000/index"
    postDict = {
        'username' : 'test',
        'password' : '123',
        'login' : 'I\'m login'
    }
    headers = {'Content-Type':'application/json'}
    request = urllib2.Request(url, headers = headers, data = json.dumps(postDict))
    request.get_method = lambda : "POST"
    response = urllib2.urlopen(request)
    print response.read()

if __name__ == '__main__':
    post()