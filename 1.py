# deb calc
    a = float(input("Первое число:"))

    z = input("Действие:")

    b = float(input("Второе число:"))

    recult = (" - результат")
    
    

if z == "+":
    c = a + b
    print(int(a) + str(z) + int(c) + recult)

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
    print("Указан не верный оператор")
    
