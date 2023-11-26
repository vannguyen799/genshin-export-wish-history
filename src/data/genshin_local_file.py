import os

from src.type import BannerType
from src.util import *


class GenshinLocalFile:
    def __init__(self, genshin_folder_path=r'C:\Program Files\Genshin Impact\Genshin Impact game'):
        # example: C:\Program Files\Genshin Impact\Genshin Impact game
        self._path = genshin_folder_path

    def _get_current_webcache_path(self):
        _wc_path = os.path.join(self._path, r'GenshinImpact_Data\webCaches')

        if os.path.isdir(_wc_path):
            list_folders = [f for f in os.listdir(_wc_path) if os.path.isdir(os.path.join(_wc_path, f))]
            list_folders.sort(key=lambda x: str(x))
            _lastest_ver = list_folders[len(list_folders) - 1]
            return _wc_path + f'\\{_lastest_ver}'
        else:
            raise ValueError(f"Can't find webCache folder: got {_wc_path}")

    def _get_data_2_content(self):
        path = self._get_current_webcache_path() + r'\Cache\Cache_Data\data_2'

        # shutil.copyfile(path, r'../runtime/data_2')
        # copy_file_path = '../runtime/data_2'
        if os.path.isfile(path):
            with open(path, 'r', encoding='utf-8', errors='ignore') as data2:
                return remove_non_printable_chars(data2.read())
        else:
            raise ValueError(f"Couldn't find data_2 file: path {path}")

    def get_banner_history_api(self):
        data = self._get_data_2_content()
        list_url = extract_links_from_text(data)
        list_url.reverse()
        for url_ in list_url:
            if r'/gacha_info/api/getGachaLog' in url_:
                return url_
        raise ValueError('Could not find character banner href')

