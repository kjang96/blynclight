import requests

data = {
        'type': 'travis',
        'status': 'ok'
}

requests.post('http://localhost:5000/blynclight', json=data)
