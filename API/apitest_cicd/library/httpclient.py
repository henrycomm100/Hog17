import requests


class HttpClient:
    """Generic HTTP Client Class"""

    def __init__(self, disable_ssl_verify=False, timeout=60):
        self.client = requests.session()
        self.disable_ssl_verify = disable_ssl_verify
        self.timeout = timeout

    def get(self, url):
        if self.disable_ssl_verify:
            response = self.client.get(url, verify=False, timeout=self.timeout)
        else:
            response = self.client.get(url, timeout=self.timeout)

        response.encoding = 'utf-8'
        print(f'{response.json()}')

        return response
