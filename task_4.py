# Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное
#  количество символов влево или вправо. При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг
# на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также
#  функцию, которая спрашивает ключ, считывает текст и дешифровывает его.

text = '''
Treasure спрятан справа от Barn
Нужно пройти ten шагов от разбитого trough
В сторону большого дуба
Затем повернуть направо
И сделать еще пять steps
Там лежит большой камень
Клад находится под ним
В сундуке находится дальнейшая instruction
'''

import string

eng_abc = string.ascii_lowercase + string.ascii_uppercase + string.punctuation
rus_abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' + string.punctuation

def crypt_text(text:str, key:int, decrypt = False):
    '''
    Функция шиврования
    '''
    new_text = ''
    key = key if not decrypt else - key

    for index, letter in enumerate(text):
        use_abc = rus_abc if letter in rus_abc else eng_abc
        letter_index = use_abc.find(letter)
        new_place = (letter_index + key) % len(use_abc)
        if letter in use_abc:
            new_text += use_abc[new_place]
        else:
            new_text += letter
    return new_text

crypted_text = crypt_text(text, 4)
print(crypted_text)
encrypted_text = crypt_text(crypted_text, 4, decrypt = True)
print(encrypted_text)