# deb calc
from colorama import init
from colorama import Fore, Back, Style

print(Fore.BLACK)
print(Back.GREEN)
a = float(input("Первое число:"))
print(Back.CYAN)
z = input("Действие:")
print(Back.YELLOW)
b = float(input("Второе число:"))
print(Back.RED)
recult = (" - результат")
    


if z == "+":
    c = a + b
    print(str(c) + recult)

elif z == "-":
    c = a - b
    print(str(c) + recult)

elif z == "*":
    c = a * b
    print(str(c) + recult)

elif z == "/":
    c = a // b
    print(str(c) + recult)


else:  # z != "+", "-", "*", "/":
    print(Back.WHITE)
    print("Указан не верный оператор")
    
input()