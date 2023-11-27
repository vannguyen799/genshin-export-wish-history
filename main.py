from src.test.test import *
from src.util import delete_exported_xlsx

# 1. Open Genshin Impact Game then open banner history
# 2. Run script

if __name__ == '__main__':
    # Set your Genshin Impact game installation location
    # -- You can find it by open Genshin Launcher -> Setting -> Game resources
    # -- Example: C:\Program Files\Genshin Impact\Genshin Impact game
    genshin_path = r'C:\Program Files\Genshin Impact\Genshin Impact game'

    user = crawl_data_test(genshin_path)

    export_xlsx_test(user.UID, ignore_3_star=False)
