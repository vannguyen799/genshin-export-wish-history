import os
from pathlib import Path


def get_project_path(name):
    path = Path(os.getcwd())
    while True:
        if path.name == name:
            return path.__str__()
        if path.parent is not None:
            path = path.parent
        else:
            raise ValueError('?? project path')

project_name = 'genshin-export-wish-history'
project_path = get_project_path(project_name)
database_folder = project_path + r'\database'
export_folder = project_path + r'\export'