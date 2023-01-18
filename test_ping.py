import requests
import responses

host = 'http://127.0.0.1:5000'
req = '/ping'


def pingRequest(host, req):
    return requests.get(host + req).status_code


def test_pingRequest():
    assert pingRequest(host, req) == 200


