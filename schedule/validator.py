import asyncio
import aiohttp

class Validator:
    def __init__(self):
        self._raw_ips = None
        self._useful_ips = None
        self._test_site = 'http://www.baidu.com'

    def recieve(self, ips):
        self._raw_ips = ips
        self._useful_ips = []


    async def _test_single(self, ip):
        print('validating proxy {}'.format(ip))
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(self._test_site, proxy='http://'+ip, timeout=15) as response:
                    self._useful_ips.append(ip)
                    print('stored useful proxy {}'.format(ip))
            except Exception as e:
                print(e)
                print('proxy {} cannot use'.format(ip))

    def test(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait([self._test_single(item) for item in self._raw_ips], loop=loop))

    @property
    def useful_proxies(self):
        return self._useful_ips

