# 5'. Реализуйте алгоритм перемешивания списка.


from random import Random, randint

N = int(input('Введите количество элекментов списка '))
list = []
for i in range(N):
    list.append(randint(-N,N+1))


def mix(list):
    newlist = list[:]
    numbers_length = len(newlist)
    for i in range(numbers_length):
        index = randint(0, numbers_length - 1)
        temp = newlist[i]
        newlist[i] = newlist[index]
        newlist[index] = temp
    return newlist
print('Исходный список')
print(list) 
print('Список после перемешивания')  
print(mix(list))