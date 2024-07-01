import requests
import json

def send_vote(url, vote_data):
    # url = 'http://localhost:8080'
    # data = {'block_id': '6fhdowieihoiwe5'}
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, data=json.dumps(vote_data), headers=headers)

    print(f"Response status code: {response.status_code}")
    print(f"Response body: {response.text}")

def send_block(url, block_data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(block_data), headers=headers)

    print(f"Response status code: {response.status_code}")
    print(f"Response body: {response.text}")

if __name__ == "__main__":
    send_vote('http://localhost:8080/vote', {'block_id': '6fhdowieihoiwe5'})
    send_block('http://localhost:8080/block', {'id': '6fhdowieihoiwe5', "view": 1})
    send_block('http://localhost:8080/block', {"view": 1})