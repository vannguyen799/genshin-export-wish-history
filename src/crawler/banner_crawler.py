from datetime import datetime

import requests
import time

from src.util import edit_url_attribute
from src.config import time_delay_per_request
from src.type import BannerType


class BannerCrawler:
    def __init__(self, api, bannerType=BannerType.CharacterBanner):
        api = edit_url_attribute(api, 'init_type', bannerType)
        api = edit_url_attribute(api, 'gacha_type', bannerType)
        api = edit_url_attribute(api, 'lang', 'en')
        self.api = api
        self._banner_type = bannerType
        self._last_crawl = None

    @property
    def CharacterBannerCrawler(self):
        return BannerCrawler(self.api, BannerType.CharacterBanner)

    @property
    def WeaponBannerCrawler(self):
        return BannerCrawler(self.api, BannerType.WeaponBanner)

    @property
    def NormalBannerCrawler(self):
        return BannerCrawler(self.api, BannerType.NormalBanner)

    def get_uid(self):
        api = self.api
        api = edit_url_attribute(api, 'page', 1)
        api = edit_url_attribute(api, 'end_id', 0)
        data_response = self.api_get_history(api)
        uid = data_response[0]['uid']

        return uid

    @staticmethod
    def api_get_history(api):
        time.sleep(time_delay_per_request)

        api = edit_url_attribute(api, 'timestamp', int(datetime.now().timestamp()))
        data_response = requests.get(api).json()
        _data = None
        try:
            _data = data_response['data']['list']
        except TypeError:
            raise ValueError(
                f'Api Err: {data_response}.\nTry load Genshin banner history on Genshin app and run again.')
        return _data

    def crawl(self, stop_end_id=-1):
        api = self.api
        history_data = []
        end_id = 0
        print('getting history data...')
        for i in range(100000):
            page = i + 1
            api = edit_url_attribute(api, 'page', page)
            api = edit_url_attribute(api, 'end_id', end_id)
            time.sleep(time_delay_per_request)
            _data = self.api_get_history(api)

            if len(_data) == 0 or int(stop_end_id) >= int(end_id) and end_id != 0:
                for h in reversed(history_data):
                    if int(h['id']) <= int(stop_end_id):
                        history_data.remove(h)
                    else:
                        break
                print(f'got {len(history_data)} update')
                break

            history_data.extend(_data)
            end_id = history_data[-1]['id']

        self._last_crawl = history_data
        return history_data

    @staticmethod
    def history_to_array(history_data: list, ignore_3_star=False):
        _hd = []
        pity_4 = 1
        pity_5 = 1
        history_data.reverse()
        for h in history_data:
            pity = 0
            if int(h['rank_type']) == 5:
                pity = pity_5
                pity_5 = 1
            else:
                pity_5 += 1
            if int(h['rank_type']) == 4:
                pity = pity_4
                pity_4 = 1
            else:
                pity_4 += 1

            if int(h['rank_type']) == 3 and ignore_3_star is True:
                continue

            _hd.append([
                h['uid'],
                h['gacha_type'],
                # h['item_id'],
                # h['count'],
                h['time'],
                h['name'],
                # h['lang'],
                h['item_type'],
                h['rank_type'],
                h['id'],
                pity
            ])

        _hd.reverse()
        return _hd
