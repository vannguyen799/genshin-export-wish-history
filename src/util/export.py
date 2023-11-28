from openpyxl import Workbook
from src import User, path_info


def export_to_paimon_moe_xlsx(user: User, output_path: str = None):
    if output_path is None:
        output_path = path_info.export_folder + f'\\{user.UID}_paimon_moe.xlsx'
    workbook = _paimon_moe_xlsx_workbook()


    for h in reversed(user.CharacterBanner):
        workbook['Character Event'].append(
            (h['item_type'], h['name'], h['time'], h['rank_type'])
        )
    for h in reversed(user.WeaponBanner):
        workbook['Weapon Event'].append(
            (h['item_type'], h['name'], h['time'], h['rank_type'])
        )
    for h in user.NormalBanner.__reversed__():
        workbook['Standard'].append(
            (h['item_type'], h['name'], h['time'], h['rank_type'])
        )

    workbook.save(output_path)
    return output_path


def _paimon_moe_xlsx_workbook():
    workbook = Workbook()
    workbook.create_sheet('Information')
    workbook.create_sheet('Character Event')
    workbook.create_sheet('Weapon Event')
    workbook.create_sheet('Standard')
    workbook.create_sheet("Beginners' Wish")

    workbook['Information'].append(('Paimon.moe Wish History Export',))
    workbook['Information'].append(('Version', '3'))
    workbook['Information'].append(('Export Date', '3'))
    header = ('Type', 'Name', 'Time', '⭐', 'Pity', '#Roll', 'Group', 'Banner', 'Part')
    workbook['Character Event'].append(header)
    workbook['Weapon Event'].append(header)
    workbook['Standard'].append(header)
    return workbook
