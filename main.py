from src.test.test import *
from src.util.export import *

# 1. Open Genshin Impact Game then open banner history
# 2. Run script

if __name__ == '__main__':

    user = crawl_data_test(genshin_path=None)

    export_to_paimon_moe_xlsx(user)

    export_xlsx_test(user.UID, ignore_3_star=False)
