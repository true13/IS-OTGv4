import requests

if __name__ == "__main__":
    req = requests.get("https://jbnu.ac.kr/")

    print(req.headers['Server'])