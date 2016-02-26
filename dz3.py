# coding: utf-8

#База Данных по студентам.

data = {'Егор Корольчук',
        'Юрий Рябов',
        'Денис Циганов',
        'Андрей Лекарев',
        'Жека Fm',
        'Кирилл Сухарев',
        'Антон Кожанов',
        'Андрей Андреев',
        'Виталий Маковкин',
        'Настя Захарина',
        'Дмитрий Синицкий',
        'In  Effect',
        'Даниил Ершов',
        'Ишхан Никогосян',
        'Vensder Fainas',
        'Павел Логинов',
        'Александр Бутаков',
        'Даниил Савицкий',}
import pickle

with open('data.pickle', 'wb') as f:
     pickle.dump(data, f)
with open('data.pickle', 'rb') as f:
     data_new = pickle.load(f)
     print(data_new)
print('-'*80)

#Фильтр

def func():
    a=input('Введите имя или фамилию:')
    i=0
    for name in data:
        x=name.split()
        for b in x:
            if b==a:
                print(x)
                i=i+1
    if i==0:
        print('Нет такого имени или фамилии.Введите заново:')
        func()        
func()
