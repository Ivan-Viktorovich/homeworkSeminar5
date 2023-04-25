# Задача 26:  Посчитать факториал (произведение 1 до N) 
# и треугольное число (сумма чисел от 1 до N) для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов

def factorial(n):
    if n == 1:
        return n
    else:
        if a == 1:
            n = n * (factorial(n-1))
            print(n)
            return n
        else:
            n = n + (factorial(n-1))
            print(n)
            return n

n = int(input("Введите число: "))
a = int(input("Выбери что нужно поситать: факториал - 1; треуголник - 2: "))
factorial(n)