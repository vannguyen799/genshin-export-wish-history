from src.path_info import database_folder, export_folder
from src.util import util
from src.model import User


def _query_list_user_uid():
    db_user_file_list = util.get_file_names(f'{database_folder}/user')
    uid_list = []
    for value in db_user_file_list:
        [f_name, f_ext] = value.split('.')
        if f_ext == 'json':
            try:
                int(f_name)
                if len(f_name) == 9:
                    uid_list.append(f_name)
            except Exception:
                pass
    return uid_list


class UsersManager:
    def __init__(self):
        pass

    @staticmethod
    def get_users() -> list[User]:
        uid_list = _query_list_user_uid()
        uid_list.remove('000000000')
        return [User(uid) for uid in uid_list]



if __name__ == '__main__':
    print(_query_list_user_uid())