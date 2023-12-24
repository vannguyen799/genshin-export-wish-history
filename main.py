from src import GenshinWishExport
from src.util import export
# 1. Open Genshin Impact Game then open banner history
# 2. Run script

if __name__ == '__main__':
    gensin_folder_path = None
    history_api = None

    genshin_export = GenshinWishExport(genshin_folder_path=gensin_folder_path, history_api=gensin_folder_path)

    print(genshin_export.get_uid())

    user = genshin_export.crawl()

    user.export_xlsx(ignore_3_star=False, output_path=None)

    export.export_to_paimon_moe_xlsx(user, output_path=None)


