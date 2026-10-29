def is_palindrome(marker: str) -> bool:
    marker = marker.strip()
    return marker == marker[::-1]
    

usinput = input("введи маркер:  ")
if is_palindrome(usinput):
    print("Палиндром — подозрительный маркер")
else:
    print("норм")
