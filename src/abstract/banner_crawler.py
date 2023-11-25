import requests
import time

from src.util import edit_url_attribute


class BannerCrawler:
    def __init__(self, api):
        self._api = api

        self._last_crawl = None

    def crawl(self, stop_end_id=-1):
        api = self._api
        history_data = []
        end_id = 0
        print('getting history data...')
        for i in range(100):
            page = i + 1

            api = edit_url_attribute(api, 'page', page)
            api = edit_url_attribute(api, 'end_id', end_id)
            data_response = requests.get(api).json()
            _data = data_response['data']['list']
            if len(_data) == 0:
                break
            if stop_end_id >= int(end_id):
                break

            history_data.extend(_data)
            end_id = history_data[-1]['id']

            time.sleep(1)
        self._last_crawl = history_data
        return history_data

    @staticmethod
    def history_to_array(history_data):
        _hd = []
        for h in history_data:
            _hd.append([
                h['uid'],
                h['gacha_type'],
                h['item_id'],
                h['count'],
                h['time'],
                h['name'],
                h['lang'],
                h['item_type'],
                h['rank_type'],
                h['id'],
            ])
        return _hd
