# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов 
# исходной последовательности. Не использовать множества.
# Постарайтесь решить за одно условие
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

from random import randrange

def random_list(list_size) -> int:
    '''
    Фунция вывода списка случайных чисел
    '''
    list_rand = list()
    for i in range(list_size):
        list_rand.append(randrange(1, 5, 1))
        list_rand = sorted(list_rand)
    return list_rand

def sorting_list(list1):
    '''
    Функция сортировки: удаление повторяющихся елементов
    '''
    list_result = []
    
    for i in list1:
        if i not in list_result:
            list_result.append(i)       
    return list_result    

ran_list = random_list(9)
res_list = sorting_list(ran_list)
print(f'Список случайных чисел: {ran_list}')
print(f'Отсортированный список: {res_list}')
