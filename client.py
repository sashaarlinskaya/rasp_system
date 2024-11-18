import requests

def make_request():
    data = {
        "certificate": open('client_cert.pem', 'r').read(),
        "data": "some_data"
    }

    s = requests.Session()
    s.verify = 'ca_cert.pem'
    s.cert = ('client_cert.pem', 'client_key.pem')

    try:
        response = s.post('https://localhost:5000/api/data', json=data)

        if response.status_code == 200:
            print(response.json())
        else:
            print(f"Error: {response.status_code} - {response.text}")

    except requests.exceptions.SSLError as ssl_error:
        print(f"SSL error: {ssl_error}")
    except requests.exceptions.RequestException as req_error:
        print(f"Request error: {req_error}")

if __name__ == '__main__':
    make_request()
