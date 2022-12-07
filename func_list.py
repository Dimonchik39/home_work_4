from typing import List

def list_data(file_name: str) -> List[str]:
    '''
    Функция возврата списка из строк файла
    '''
    with open(file_name, encoding='utf-8') as file:
        return file.read().split('\n')
        