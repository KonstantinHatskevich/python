#6. Если фирма отработала с прибылью, вычислите рентабельность выручки.
#Это отношение прибыли к выручке. Далее запросите численность сотрудников
#фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

a = int(input("Введите сумму выручки:"))
b = int(input("Введите сумму издержек:"))

if a > b:
    print(f"Результат фин. работы - прибыль: {a - b}")
    print(f"Рентабельность выручки: {(a - b) / a}")
else:
    print(f"Результат фин. работы - убыток: {b - a}")

c = int(input("Введите кол-во сотрудников:"))
print(f"Прибыль фирмы на одного сотрудника: {round(a / c, 2)}")