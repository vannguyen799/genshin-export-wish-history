import os
from pathlib import Path

database_folder = Path(os.getcwd()).parent.__str__() + r'\database'
export_folder = Path(os.getcwd()).parent.__str__() + r'\export'