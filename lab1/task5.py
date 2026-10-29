def is_magic_number(number: int) -> bool:
    if number % 7 == 0:
        return True
    return False

def count_summ(number: int) -> int:
    summ = 0
    while number > 0:
        summ += number % 10
        number //= 10
    return summ
        
def main():
    number_str = input("Введите число:  ")
    number = int(number_str)
    if (is_magic_number(number)):
        print("Магическое число!")
        return
    print(f"Сумма цифр числа {number}: {count_summ(number)}")

if __name__ == "__main__":
    main()
