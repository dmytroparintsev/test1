num1 = float(input("Введіть перше число: "))
op = input("Введіть дію (+, -, *, /): ")
num2 = float(input("Введіть друге число: "))

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 == 0:
        print("Помилка: ділення на нуль!")
    else:
        result = num1 / num2
else:
    print("Невідома дія!")
    result = None

if result is not None:
    print("Результат:", result)

