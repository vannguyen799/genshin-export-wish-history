from src.abstract import BannerCrawler


class CharacterBannerCrawler(BannerCrawler):
    def __init__(self, api):
        super().__init__(api)
