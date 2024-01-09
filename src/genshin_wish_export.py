from .model import User, UsersManager
from .data import GenshinLocalFile
from .crawler import BannerCrawler


class GenshinWishExport:
    history_api: str | None
    genshin_folder_path: str | None

    def __init__(self, genshin_folder_path=None, history_api=None):
        self.genshin_folder_path = genshin_folder_path
        self.genshin_local_file = GenshinLocalFile(genshin_folder_path)
        self.set_history_api(history_api)

        self.banner_crawler = BannerCrawler(self.history_api)
        self.user_manager = UsersManager()

    def set_history_api(self, api=None):
        if api is None:
            api = self.genshin_local_file.get_banner_history_api()
        self.history_api = api
        return self

    def get_users(self) -> list[User]:
        return self.user_manager.get_users()

    def get_uid(self, _history_api=None):
        if _history_api:
            self.banner_crawler.api = _history_api
        else:
            self.banner_crawler.api = self.history_api

        return self.banner_crawler.get_uid()

    def crawl(self,
              _history_api=None,
              character_banner=True,
              normal_banner=True,
              weapon_banner=True):
        if _history_api:
            self.banner_crawler.api = _history_api
        else:
            self.banner_crawler.api = self.history_api

        user = User(self.get_uid())
        user.set_api_url(self.banner_crawler.api)
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
