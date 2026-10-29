def count_exchange(summ: int, banknotes: list) -> dict:
    exchange_banknotes = {}
    for banknote in banknotes:
        count = summ // banknote
        if count > 0:
            exchange_banknotes[banknote] = count
        summ = summ % banknote
    return exchange_banknotes


summ = int(input("Введите сумму рублей:  "))
banknotes = [100, 50, 10, 5, 2, 1]
exchange = count_exchange(summ, banknotes)
print(f"Размен для {summ} рублей: ")
for banknote, count in exchange.items():
    print(f"{banknote} рублей: {count} штуки")