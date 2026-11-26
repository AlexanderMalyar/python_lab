import sys
import math
from pathlib import Path

def input_check() -> str:
    if len(sys.argv) < 2:
        sys.stderr.write("Ошибка: не указан путь к файлу\n")
        sys.exit(1)
    file_path = Path(sys.argv[1])
    if not file_path.exists():
        sys.stderr.write(f"Ошибка: файл {file_path} не найден")
        sys.exit(1)
    return file_path

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    file_path = input_check()
    stats = {}
    with open(file_path, 'r', encoding = 'utf-8') as _file:
        for line in _file:
            station, temper_str = line.strip().split(';')