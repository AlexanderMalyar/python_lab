import random

code = random.randint(1, 100)
print("угадай код")
while True:
    guess = input("ввод:  ")
    if not guess.isdigit():
        print("ошибка, введи число")
        continue
    if int(guess) < code:
        print("больше")
    elif int(guess) > code:
        print("меньше")
    else:
        print("код подобран")
        break