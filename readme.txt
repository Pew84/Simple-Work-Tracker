компиляции в один exe файл:
в терминале: pyinstaller --onefile --windowed main.py

pyinstaller --windowed --onefile --add-data "font;" main.py

pyinstaller --windowed --onefile --add-data ".venv\Lib\site-packages\tkextrafont;tkextrafont" main.py

pyinstaller --windowed --icon=faviconico.ico --onefile --add-data ".venv\Lib\site-packages\tkextrafont;tkextrafont" main.py