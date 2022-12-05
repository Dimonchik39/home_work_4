# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

def give_int(input_number) -> int:
    '''
    Функция ввода числа
    '''
    while True:
        try:
            num = int(input(input_number))  
            return num
        except ValueError:
            print('Вы ввели не число. Введите число.')

# def multiplier_list(num):
#     i = 2 
#     res_list = []
#     while i <= num:
#         if num % i == 0:
#             res_list.append(i)
#             num //= i
#             i = 2
#         else:
#             i += 1
#     return res_list

def multiplier_list(num):
    res_list = []
    prime_num = 2
    
    while prime_num * prime_num <= num:
        if num % prime_num == 0:
            res_list.append(prime_num)
            num //= prime_num
        else:
            prime_num += 1
    res_list.append(num)
    return res_list

int_num = give_int('Введите число: ')
result_list = multiplier_list(int_num)
print(f'N = {int_num} -> {result_list}')
