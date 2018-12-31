import requests
from requests.exceptions import ConnectionError
from core.config import HEADER


def get_page(url):
    try:
        r = requests.get(url, headers=HEADER)
        if r.status_code == 200:
            return r.text
        else:
            print(r.status_code)
            return None
    except ConnectionError:
        print('net error!')
        return None

if __name__ == '__main__':
    print(get_page('http://www.baidu.com'))