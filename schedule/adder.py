from core.crawler import Crawler
from core.db import DBManager
import concurrent.futures



class Adder:
    def __init__(self):
        self._crawler = Crawler()

    def _crawl_fns(self):
        return [self._crawler.__getattribute__(fn_name) for fn_name in self._crawler.fn_names]

    def add(self):
        raw_ips = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(fn) for fn in self._crawl_fns()]
            for future in concurrent.futures.as_completed(futures):
                try:
                    data = future.result()
                    raw_ips.extend(data)
                except Exception as exc:
                    print('generated an exception:{}'.format(exc))
                else:
                    print('crawl succcess')
        return [raw_ips[i:i+100] for i in range(0, len(raw_ips), 100)]
