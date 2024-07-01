import requests
import json

def send_request(url):
    # url = 'http://localhost:8080'
    data = {'block_id': '6fhdowieihoiwe5'}
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, data=json.dumps(data), headers=headers)

    print(f"Response status code: {response.status_code}")
    print(f"Response body: {response.text}")

if __name__ == "__main__":
    send_request('http://localhost:8080/vote')