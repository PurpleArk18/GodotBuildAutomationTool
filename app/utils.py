from pathlib import Path
from enum import Enum
import subprocess

SCRIPT_PATH = Path(__file__).resolve().parent

RESOURCE_PATH = Path(SCRIPT_PATH) / "rsc"
ICONS_PATH = RESOURCE_PATH / "icons" / "icons"

QT_UI_PATH = Path(SCRIPT_PATH) / "view" / "qt6" / "modules" / "ui" / "module1.ui"

HELPER_PATH = Path(SCRIPT_PATH) / "helper.ui"

FILE_FILTERS = [
    "Portable Network Graphics files (*.png)",
    "Text files (*.txt)",
    "Comma Separated Values (*.csv)",
    "JSON file (*.json)",
    "All files (*.*)",
]

class FileFilter(Enum):
    PNG = 0
    TXT = 1
    CSV = 2
    ALL = 3

default_filter = FILE_FILTERS[3]

filters = ';;'.join(FILE_FILTERS)

def get_icon_path(name):
    result = str(Path(ICONS_PATH) / name)
    print(result)
    return result

def get_filter_string(filter_enum):
    return FILE_FILTERS[filter_enum.value]

def get_module_file():
    return str(QT_UI_PATH)
