from .model import User, UsersManager
from .data import GenshinLocalFile
from .crawler import BannerCrawler

class GenshinWishExport:
    history_api: str | None = None

    def __init__(self, genshin_folder_path=None, history_api=None):
        self.history_api = history_api
        self.genshin_folder_path = genshin_folder_path

        self.genshin_local_file = GenshinLocalFile(genshin_folder_path)
        self.banner_crawler = BannerCrawler(history_api)

        self.user_manager = UsersManager()

        pass

    def set_history_api(self, api=None):
        self.history_api = api

    def get_users(self) -> list[User]:
        return self.user_manager.get_users()

    def get_uid(self, _history_api=history_api):
        if _history_api:
            self.banner_crawler.api = _history_api
        return self.banner_crawler.get_uid()

    def crawl(self,
              _history_api=history_api,
              character_banner=True,
              normal_banner=True,
              weapon_banner=True):
        if _history_api:
            self.banner_crawler.api = _history_api

        user = User(self.get_uid(_history_api))

        if character_banner:
            user.set_character_banner(
                self.banner_crawler.CharacterBannerCrawler.crawl(user.get_last_character_banner_id())
            ).save()
        if weapon_banner:
            user.set_weapon_banner(
                self.banner_crawler.WeaponBannerCrawler.crawl(user.get_last_weapon_banner_id())
            ).save()
        if normal_banner:
            user.set_normal_banner(
                self.banner_crawler.NormalBannerCrawler.crawl(user.get_last_normal_banner_id())
            ).save()
        return user




