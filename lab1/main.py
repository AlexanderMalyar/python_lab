import sys
import math
from pathlib import Path

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    if len(sys.argv) < 2:
        sys.stderr.write("Ошибка: не указан путь к файлу\n")
        sys.exit(1)
    file_path = Path(sys.argv[1])
    if not file_path.exists():
        sys.stderr.write(f"Ошибка: файл {file_path} не найден")
        sys.exit(1)
    stats = {}
    with open(file_path, 'r', encoding = 'utf-8') as _file:
        for line in _file:
            station, temper_str = line.strip().split(';')
            temper = float(temper_str)
            if station in stats:
                mintemp, maxtemp, total, count = stats[station]
                stats[station] = [
                    min(mintemp, temper),
                    max(maxtemp, temper),
                    total + temper,
                    count + 1
                ]
            else:
                stats[station] = [temper, temper, temper, 1]
    for station in sorted(stats.keys()):
        mintemp, maxtemp, total, count = stats[station]
        mean = total / count
        rounded_mean = math.floor(10 * mean + 0.5) / 10
        print(f"{station};{mintemp:.1f};{rounded_mean:.1f};{maxtemp:.1f}")

if __name__ == '__main__':
    main()