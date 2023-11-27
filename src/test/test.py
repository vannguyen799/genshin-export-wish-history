from src.data import GenshinLocalFile
from src.model import User
from src.crawler import *


def export_xlsx_test(uid, ignore_3_star=False):
    user = User(uid)
    user.export_xlsx(ignore_3_star=ignore_3_star)


def crawl_data_test(genshin_path=r'C:\Program Files\Genshin Impact\Genshin Impact game'):
    GLF = GenshinLocalFile(genshin_path)
    api = GLF.get_banner_history_api()
    print(api)

    CBC = CharacterBannerCrawler(api)
    WBC = WeaponBannerCrawler(api)
    NBC = NormalBannerCrawler(api)

    uid = CBC.get_uid()
    user = User(uid)
    print(f'uid {uid}')
    history_data = CBC.crawl(user.get_last_character_banner_id())
    user.set_character_banner(history_data).save()
    history_data = WBC.crawl(user.get_last_weapon_banner_id())
    user.set_weapon_banner(history_data).save()
    history_data = NBC.crawl(user.get_last_normal_banner_id())
    user.set_normal_banner(history_data).save()
