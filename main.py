user_number = input("Введіть 4-х значне число:")
number = int(user_number)
a = number // 1000
b = (number % 1000) // 100
c = (number % 100) // 10
d = (number % 10)
print(a)
print(b)
print(c)
print(d)