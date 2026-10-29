def checkpass(password: str) -> str:
    if len(password) < 16:
        return f"Слишком короткий"
    has_letter = any(i.isalpha() for i in password)
    has_digit = any(i.isdigit() for i in password)
    if has_digit and has_letter:
        return "надежный пароль"
    else:
        return "слабый пароль"
        
user_input = input("Введите пароль:  ")
print(checkpass(user_input))