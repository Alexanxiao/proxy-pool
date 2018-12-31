from .downloader import get_page
import re
import time

class Crawler:

    @property
    def fn_names(self):
        return ['xici', 'kuaidaili',  'ip3366', 'jiangxianli']

    def pasrse(self, baseurls, pattern, pages):
        ips = []
        for baseurl in baseurls:
            for i in range(1, pages+1):
                source = baseurl+str(i)
                html = get_page(source)
                if html is not None:
                    for data in re.findall(pattern, html):
                        print('fetch {}:{}'.format(data[0], data[1]))
                        ips.append('{}:{}'.format(data[0], data[1]))
        return ips


    def xici(self, pages=5):
        baseurls = ['http://www.xicidaili.com/nn/', 'http://www.xicidaili.com/nt/']
        pattern = r'<td>(\d+\.\d+\.\d+\.\d+)</td>\s*<td>(\d+)</td>'
        return self.pasrse(baseurls, pattern, pages)

    def kuaidaili(self, pages=4):
        baseurls = ['https://www.kuaidaili.com/free/inha/', 'https://www.kuaidaili.com/free/intr/']
        pattern = r'<td data-title="IP">(.*?)</td>\s*<td data-title="PORT">(\d+)</td>'
        ips = []
        for baseurl in baseurls:
            for i in range(1, pages + 1):
                source = baseurl + str(i)
                html = get_page(source)
                time.sleep(1)
                for data in re.findall(pattern, html):
                    print('fetch {}:{}'.format(data[0], data[1]))
                    ips.append('{}:{}'.format(data[0], data[1]))
        return ips

    def ip3366(self, pages=3):
        baseurls = ['http://www.ip3366.net/free/?stype=1&page=', 'http://www.ip3366.net/free/?stype=2&page=',
                    'http://www.ip3366.net/free/?stype=3&page=']
        pattern = r'<td>(\d+\.\d+\.\d+\.\d+)</td>\s*<td>(\d+)</td>'
        return self.pasrse(baseurls, pattern, pages)

    def jiangxianli(self, pages=30):
        baseurls = ['http://ip.jiangxianli.com/?page=']
        pattern = r'<td>(\d+\.\d+\.\d+\.\d+)</td>\s*<td>(\d+)</td>'
        return self.pasrse(baseurls, pattern, pages)

