# deb calc
while True:
    a = float(input("Первое число:"))

    z = input("Действие:")

    b: float = float(input("Второе число:"))
    if a.lower() == "Exit":
        break

if z == "+":
    c = a + b
    print(int(a) + str(z) + int(c) + '  - результат')

elif z == "-":
    c = a - b
    print(str(c) + " - результат")

elif z == "*":
    c = a * b
    print(str(c) + " - результат")

elif z == "/":
    c = a // b
    print(str(c) + " - результат")

else:  # z != "+", "-", "*", "/":
    print("Указан не верный оператор")
