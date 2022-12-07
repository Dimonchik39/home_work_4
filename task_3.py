# В файле, содержащем фамилии студентов и их оценки, 
# изменить на прописные буквы фамилии тех студентов, 
# которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Энакин Скайуокер 5
# Фредди Меркури 3
# Александр Пушкин 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# ЭНАКИН СКАЙУОКЕР 5
# Фредди Меркури 3
# Александр Пушкин 4

from typing import List
from func_list import list_data

def caps_lock(list1: list, cond_str: str) -> List[str]:
    '''
    Функция отбора строк по критериям 
    '''
    for i in range(len(list1)):
        if cond_str in list1[i]:
            list1[i] = list1[i].upper()
    return list1

list1 = list_data('/Users/dima/Documents/обучение/Изучение_Python/Домашка/DZ_4_PY/student.txt')

print('\n'.join(caps_lock(list1, '5')))

# with open('/Users/dima/Documents/обучение/Изучение_Python/Домашка/DZ_4_PY/student.txt', 'w', encoding='utf-8') as data1:
#     for i in range(len(list1)):
#         data1.writelines(f'{list1[i]}\n')