import datetime
import json
import os

from static.path_info import database_folder


class User:
    UID = 000000000

    def __init__(self, uid=UID):
        self.UID = uid
        self.path = f'{database_folder}\\user\\{self.UID}'
        self._data = None
        self.CharacterBanner = []
        self.WeaponBanner = []
        self.NormalBanner = []

    def set_character_banner(self, history_data):
        self.CharacterBanner = self.add_history_data(self.CharacterBanner, history_data)
        return self

    def set_weapon_banner(self, history_data):
        self.WeaponBanner = self.add_history_data(self.WeaponBanner, history_data)
        return self

    def set_normal_banner(self, history_data):
        self.NormalBanner = self.add_history_data(self.NormalBanner, history_data)
        return self

    def read(self):
        if os.path.isfile(self.path):
            with open(self.path, 'r', encoding='utf-8', errors='ignore') as u:
                self._data = json.loads(u.read())
                self.CharacterBanner = self._data['wish_history']['character_banner']
                self.WeaponBanner = self._data['wish_history']['weapon_banner']
                self.NormalBanner = self._data['wish_history']['normal_banner']
        return self

    def __dict__(self):
        user_dict = {
            'uid': self.UID,
            'wish_history': {
                'character_banner': self.CharacterBanner,
                'weapon_banner': self.WeaponBanner,
                'normal_banner': self.NormalBanner,
            },
            'time': datetime.datetime.now()
        }
        return user_dict

    def save(self):
        with open(self.path, 'w', encoding='utf-8', errors='ignore') as u:
            json.dump(self.__dict__(), u)
        return self

    @staticmethod
    def add_history_data(cur_arr: list, add_arr: list):
        new_arr = add_arr
        _cur_arr = cur_arr
        for item in cur_arr:
            if item in add_arr:
                _cur_arr.remove(item)
        new_arr.extend(_cur_arr)
        return new_arr

