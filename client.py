import requests
import json
import sys

def send_vote(url, vote_data):
    # url = 'http://localhost:8080'
    # data = {'block_id': '6fhdowieihoiwe5'}
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, data=json.dumps(vote_data), headers=headers)

    print(f"Sent vote: {vote_data}")
    print(f"Response status code: {response.status_code}")
    print(f"Response body: {response.text}")

def send_block(url, block_data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(block_data), headers=headers)
    print(f"Sent block: {block_data}")
    print(f"Response status code: {response.status_code}")
    print(f"Response body: {response.text}")

if __name__ == "__main__":
    try:
        json_fpath = sys.argv[1]
    except:
        exit("Please specify input json file")
    # print(json_fpath)
    
    try:
        url = sys.argv[2]
    except:
        url = 'http://localhost:8080/'
    
    with open(json_fpath, 'r') as inputfp:
        input_list = json.load(inputfp)
    # print(data)

    for payload in input_list:
        # ignore any item with invalid format
        # format should be one of:
        #   (1) block: {"id":"string", "view":int}
        #   (2) vote:  {"block_id":"string"}
        # print(payload)
        # print(type(payload))
        if ("id" in payload.keys() and "view" in payload.keys()):
            send_block(url + "block", payload)
        elif ("block_id" in payload.keys()):
            send_vote( url + "vote", payload)
        else:
            pass
