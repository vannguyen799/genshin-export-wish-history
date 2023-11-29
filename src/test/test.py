from src.data import GenshinLocalFile
from src.model import User
from src.crawler import *


def export_xlsx_test(uid, ignore_3_star=False):
    user = User(uid)
    exported_path = user.export_xlsx(ignore_3_star=ignore_3_star)
    print(f'Open this file to view exported data: {exported_path}')


def crawl_data_test(genshin_path=None):
    GLF = GenshinLocalFile(genshin_path)
    api = GLF.get_banner_history_api()
    print(api)

    bannerCrawler = BannerCrawler(api)

    uid = bannerCrawler.get_uid()
    user = User(uid)
    print(f'uid {uid}')
    history_data = bannerCrawler.CharacterBannerCrawler.crawl(user.get_last_character_banner_id())
    user.set_character_banner(history_data).save()
    history_data = bannerCrawler.WeaponBannerCrawler.crawl(user.get_last_weapon_banner_id())
    user.set_weapon_banner(history_data).save()
    history_data = bannerCrawler.NormalBannerCrawler.crawl(user.get_last_normal_banner_id())
    user.set_normal_banner(history_data).save()
    return user
