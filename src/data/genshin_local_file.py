import os

from src.util import *
from src.path_info import *


class GenshinLocalFile:
    def __init__(self, genshin_folder_path=None):
        # example: C:\Program Files\Genshin Impact\Genshin Impact game
        if genshin_folder_path is None:
            genshin_folder_path = self._find_genshin_path()
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

        if os.path.isfile(path):
            new_path = f'{project_path}\\src\\data\\data_2'
            copy_file_powershell(path, new_path)
            with open(new_path, 'r', encoding='utf-8', errors='ignore') as data2:
                return remove_non_printable_chars(data2.read()).replace('1/0/', ' ')
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

    @staticmethod
    def _find_genshin_path():
        path = os.environ['USERPROFILE'] + r'\AppData\LocalLow\miHoYo\Genshin Impact\output_log.txt.last'
        if os.path.isfile(path):
            with open(path, 'r', encoding='utf-8') as output_log:
                paths = extract_path_from_text(output_log.read())
                for p in paths:
                    if 'Genshin Impact game/GenshinImpact_Data/' in p:
                        g = get_parent_path('Genshin Impact game', path=Path(p))
                        print(f'genshin path: {g}')
                        if g is not None:
                            return g
        else:
            raise Exception('Could not find genshin path')

        path = os.environ['USERPROFILE'] + r'\AppData\LocalLow\miHoYo\Genshin Impact\output_log.txt'
        if os.path.isfile(path):
            with open(path, 'r', encoding='utf-8') as output_log:
                paths = extract_path_from_text(output_log.read())
                for p in paths:
                    if 'Genshin Impact game/GenshinImpact_Data/' in p:
                        g = get_parent_path('Genshin Impact game', path=Path(p))
                        print(f'genshin path: {g}')
                        if g is not None:
                            return g
        else:
            raise Exception('Could not find genshin path')

    @staticmethod
    def find_uid():
        path = os.environ['USERPROFILE'] + r'\AppData\LocalLow\miHoYo\Genshin Impact\info.txt'
        if os.path.isfile(path):
            with open(path, 'r', encoding='utf-8') as info_txt:
                info = info_txt.read()
                _index = info.index('uid:')
                return info[_index + 4:][:9]
        else:
            raise Exception('Could not find genshin path')


if __name__ == '__main__':
    print(GenshinLocalFile._find_genshin_path())