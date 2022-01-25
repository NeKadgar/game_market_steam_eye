import requests
import time

from steam.core import MAX_REQUESTS_PER_MINUTE


class SteamClient:
    def __init__(self, cookies: dict):
        self._cookies = cookies
        self._session = requests.Session()
        self._timer = time.time()
        self._requests_count = 0

    def get(self, url, cookies=False, **kwargs):
        time_diff = time.time() - self._timer
        if self._requests_count == MAX_REQUESTS_PER_MINUTE and time_diff < 60:
            time.sleep(60-time_diff)
            self._timer = time.time()
            self._requests_count = 0
        self._requests_count += 1
        if cookies:
            return self._session.get(url, cookies=self._cookies, **kwargs)
        return self._session.get(url, **kwargs)
