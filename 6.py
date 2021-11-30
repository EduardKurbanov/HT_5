"""
6. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.

   P.S. Повинен вертатись генератор.

   P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range
"""


def new_rangr(start=0, stop=0, step=1):
    i = start
    if start < stop:
        while i < stop:
            yield i
            i += step
    elif start > stop:
        while i > stop:
            yield i
            i += step
    else:
        raise Exception

for i in new_rangr(0 ,10, 2):
    print(i)
