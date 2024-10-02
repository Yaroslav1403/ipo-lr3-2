number_1=float(input("Введите первое число: "))
number_2=float(input("Введите втрое число: "))
if number_1 > number_2:
    print(f"Второе число: {number_2} < Первого числа: {number_1}")
elif number_2 > number_1:
    print(f"Первое число: {number_1} < Второго числа: {number_2}")
else:
     print(f"Первое число: {number_1} = Второму числу: {number_2}")
