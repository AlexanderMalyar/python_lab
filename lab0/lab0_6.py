APRIL = 4
def zodiac_sign(birth_year: str) -> str:
    parts = birth_year.strip().split('.')
    if len(parts) != 2:
        return None
    day = int(parts[0])
    month = int(parts[1])
    if month < 1 or month > 12 or day < 1 or day > 31:
        return None
    if month == 2 and day > 28:
        return None
    if month in [APRIL, 6, 9, 11] and day > 30:
        return None
    zodiacs = [
        (21, 3, 19, 4, "овен"),
        (20, 4, 20, 5, "телец"),
        (21, 5, 20, 6, "близнецы"),
        (21, 6, 22, 7, "рак"),
        (23, 7, 22, 8, "лев"),
        (23, 8, 22, 9, "дева"),
        (23, 9, 22, 10, "весы"),
        (23, 10, 21, 11, "скорпион"),
        (22, 11, 21, 12, "стрелец"),
        (22, 12, 19, 1, "козерог"),
        (20, 1, 18, 2, "водолей"),
        (19, 2, 20, 3, "рыбы")
    ]
    for fd, fm, ld, lm, name in zodiacs:
        if (month == fm and day >= fd) or (month == lm and day <=ld):
            return name
    

usinput = input("введите дату рождения вида дд.мм:  ")
if zodiac_sign(usinput):
    print(f"{zodiac_sign(usinput)}. Не используйте это как ответ на контрольный вопрос!")
else:
    print("некорректная дата")