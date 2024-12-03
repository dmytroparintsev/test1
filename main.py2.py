user_number = input("Введіть 5-ти значне число: ")
number = int(user_number)
a = number % 10
b = (number // 10) % 10
c = (number // 100) % 10
d = (number // 1000) % 10
e = (number // 10000)
print(str(a) + str(b) + str(c) + str(d) + str(e))

