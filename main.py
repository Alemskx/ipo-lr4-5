x=int(input("Введи положительное число больше 1:"))
if x<=1:
    print("Неправильно введено число")
for i in range(1,x):
    if i%2 != 0:
        print("Нечетные числа: ",i)