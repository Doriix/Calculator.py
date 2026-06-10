a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
op = input("Wybierz operację (+, -, *, /): ")

if op == "+":
    print(f"Wynik: {a + b}")
elif op == "-":
    print(f"Wynik: {a - b}")
elif op == "*":
    print(f"Wynik: {a * b}")
elif op == "/":
    if b != 0:
        print(f"Wynik: {a / b}")
    else:
        print("Nie dziel przez zero!")
