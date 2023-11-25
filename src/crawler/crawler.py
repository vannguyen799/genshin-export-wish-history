from src.abstract import BannerCrawler
from src.type import BannerType


class CharacterBannerCrawler(BannerCrawler):
    def __init__(self, api):
        super().__init__(api, BannerType.CharacterBanner)


class WeaponBannerCrawler(BannerCrawler):
    def __init__(self, api):
        super().__init__(api, BannerType.WeaponBanner)


class NormalBannerCrawler(BannerCrawler):
    def __init__(self, api):
        super().__init__(api, BannerType.NormalBanner)