"""
Напишите функцию группового переименования файлов. Она должна:
a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
"""

import os
from Work_with_files.Seminar_file5 import generate_with_dictionary


def rename_files(directory, zero_count, ext, new_ext, name_range, wish_name=''):
    """Функция переименовывает заданные файлы указанным в параметрах образом"""
    count = 1
    for f in os.listdir(directory):
        extension = f.rsplit('.')[-1]
        if extension != ext:
            continue
        current_name = f.rsplit('.')[0]
        name_length = len(current_name)
        start = (0 if name_range[0] - 1 >= name_length else name_range[0] - 1)
        stop = (name_length if name_range[1] > name_length else name_range[1])
        trunc_name = current_name[start:stop]
        index = str(count).rjust(zero_count, '0')
        new_name = trunc_name + wish_name + index + '.' + new_ext
        count += 1
        os.rename(f'{directory}/{f}',
                  f'{directory}/{new_name}')


if __name__ == '__main__':
    d = {
        'doc': 5,
        'jpg': 5,
        'png': 5,
        'txt': 5,
    }
    generate_with_dictionary(d)
    rename_files('files', 3, 'jpg', 'png', [1, 3], wish_name='new')
