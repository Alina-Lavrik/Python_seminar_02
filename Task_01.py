# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# Пример:
# Для N = 5: 1, -3, 9, -27, 81

print('Введите число N: ')
N = int(input())

for i in range(0, N):
    print((-3)**i, end = ' ') 



