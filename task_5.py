# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# 12A11B10C6D5E4FG python is s7o c7ol

from func_list import list_data2

def compress_file(text):
    '''
    Функция сжатия данных
    '''
    comp_res = ''
    i = 0

    while i < len(text):
        count = 1
        while i + 1 < len(text) and text[i] == text[i + 1]:
            count += 1
            i += 1
        comp_res += str(count) + text[i]
        i += 1
    return comp_res

def unzip(text2):
    '''
    Функция восстановления данных после сжатия
    '''
    decomp_res = ''
    num = ''
    for i in text2:
        if i.isdigit():
            num += i
        else:
            decomp_res = decomp_res + i * int(num)
            num = ''
    return decomp_res

text_file = list_data2('/Users/dima/Documents/обучение/Изучение_Python/Домашка/DZ_4_PY/enter_text.txt')

compress = compress_file(text_file)
decompress = unzip(compress)
print(compress)
print(decompress)

with open('/Users/dima/Documents/обучение/Изучение_Python/Домашка/DZ_4_PY/compress_result.txt', 'w', encoding='utf-8') as data2:
    for i in range(len(compress)):
        data2.writelines(f'{compress[i]}')
