import requests

def login_to_match_trade(username: str, password: str) -> str | None:
    url = "https://mt-provisioning-client-api-v1.cloud.match-trade.com/api/auth/login"
    payload = {"username": username, "password": password}
    try:
        res = requests.post(url, json=payload)
        if res.status_code == 200 and "token" in res.json():
            return res.json()["token"]
        return None
    except Exception as e:
        print(f"Login error: {e}")
        return None
