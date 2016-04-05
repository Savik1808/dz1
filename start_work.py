#
# 1) Дана функция, ищущая все файлы с заданным расширением в заданной папке:

from os import listdir
from os.path import isfile
from os.path import join as joinpath

def find_files_with_ext(path, ext):
    
    mypath = 'content'
    for fi in os.listdir(mypath):
        if isfile(joinpath(mypath,i)):
            print(i)


# - Исправьте эту функцию соответственно ее назначению.
# - выдавайте полное имя файла.




# 2. Сделайте из функции find_files_with_ext генератор



# 3. Дана функция, которая находит сумму всех чисел, найденных
# в словаре.

def sum_dict_numbers( d ):
    a = 0
    for key in d:
        a += d[ key ]


# - добавьте проверку типа так, чтобы программа не ломалась при появлении
# не числа.

# - реализуете рекурсию так, чтобы посчитать в том числе и вложенные
# словари.

# - проверяйте тип вложенного объекта.



# 4. Исправьте код:

x = 1
y = 2

print( x + y )


# * 5. Что происходит в следующем коде?


def great_creater(simple = True):

    if simple:
        def new_func():
            print('simple func started')

    else:
        def new_func():
            return great_creater(True)()

    return new_func


# 6. Напишите функцию, которая выведет на экран все файлы
# из заданной папки, отсортировав по расширению.



