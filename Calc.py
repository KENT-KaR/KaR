try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    c = input("Введите операцию: ")
    if c == "-":
        c = a - b
    elif c == "+":
        c = a + b
    elif c == "*":
        c = a * b
    elif c == "/":
        c = a / b
    else:
        c = "Неизвестная операция"
    print(c)
except ValueError:
    print("ValueError")
except TypeError:
    print("TypeError")
except ZeroDivisionError:
    print("ZeroDivisionError")
