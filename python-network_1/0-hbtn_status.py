import requests

def fetch_and_display_status(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        print("Status:")
        print("\t- Response Code:", response.status_code)
        print("\t- Body:")
        print("\t\t", response.text)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    fetch_and_display_status(url)

