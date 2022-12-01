# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

print ('Введите натуральное число N')
number = int(input ())
factorial = 1
if number <= 0:
    print ('Вводить необходимо положительное число')
print ('[', end=" ")   
for i in range(1, number+1):
    factorial = factorial * i
    print(factorial, end=" ")
print (']')   
