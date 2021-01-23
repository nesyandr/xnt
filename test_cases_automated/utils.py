import requests


def get_url_status_code(url):
    try:
        return requests.get(url).status_code
    except Exception:
        return None
