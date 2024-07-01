import requests

def send_request():
    url = "http://localhost:8090/hello"

    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Failed response: {response.status_code}")

if __name__ == "__main__":
    send_request()