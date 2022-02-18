import requests
import time

from steam.core import MAX_REQUESTS_PER_MINUTE


class SteamClient:
    def __init__(self, cookies: dict):
        self._cookies = cookies
        self._session = requests.Session()

    def get(self, url, cookies=False, **kwargs):
        time.sleep(60/MAX_REQUESTS_PER_MINUTE)
        if cookies:
            return self._session.get(url, cookies=self._cookies, **kwargs)
        return self._session.get(url, **kwargs)
