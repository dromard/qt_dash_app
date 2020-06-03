
from PyInstaller.utils.hooks import collect_all

datas, binaries, hiddenimports = collect_all('dash_core_components')
