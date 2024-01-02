import os
import sys

from src import GenshinWishExport, UsersManager, User
from src.util import export


# 1. Open Genshin Impact Game then open banner history
# 2. Run script

def menu_choose():
    print(
        """
    1. Crawl and export current user logged in Genshin Impact
    2. See user in data base
    
    0. exit
    """
    )

    key = input("select: ")
    if key in ['0', '1', '2']:
        return key
    else:
        raise ValueError('PLEASE SELECT CORRECT SELECTION')


def user_choose(list_user: list[User]):
    for index, user in enumerate(list_user):
        print(f"""\t{index}. uid {user.UID}""")

    key = input("select: ")
    if int(key) < len(list_user):
        return key
    else:
        raise ValueError('PLEASE SELECT CORRECT SELECTION')


def user_action_choose():
    print(
        """
        1. crawl
        2. export
        3. export paimon moe
        4. show api
        """
    )

    key = input("select: ")
    if key in ['1', '2', '3', '4']:
        return key
    else:
        raise ValueError('PLEASE SELECT CORRECT SELECTION')


def main():
    key = menu_choose()

    genshin_folder_path = None
    history_api = None
    genshin_export = GenshinWishExport(genshin_folder_path=genshin_folder_path, history_api=history_api)
    users_manager = UsersManager()
    match key:
        case '1':
            print(genshin_export.get_uid())
            user = genshin_export.crawl()
            user.export_xlsx(ignore_3_star=False, output_file=None)
            export.export_to_paimon_moe_xlsx(user, output_path=None)
        case '2':
            users = users_manager.get_users()
            user_key = user_choose(users)
            user = users[int(user_key)]
            action_key = user_action_choose()
            match action_key:
                case '1':
                    user_ = genshin_export.crawl(_history_api=user.api_url)
                case '2':
                    output_file = user.export_xlsx(ignore_3_star=False, output_file=None)
                    print(f'exported file: {output_file}')
                case '3':
                    output_file = export.export_to_paimon_moe_xlsx(user, output_path=None)
                    print(f'exported file: {output_file}')
                case '4':
                    print(user.api_url)

        case '3':
            print('hello')
        case '0':
            return
    main()


if __name__ == '__main__':
    # from src.model.users_manager import UsersManager
    main()
