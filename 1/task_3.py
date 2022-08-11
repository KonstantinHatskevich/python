#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = int(input("Enter number n:"))

b = int(str(n) + str(n))
c = int(str(n) + str(n) + str(n))

print(f"Сумма чисел n + nn + nnn = {n + b + c}")