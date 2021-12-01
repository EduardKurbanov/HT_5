"""
6. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.

   P.S. Повинен вертатись генератор.

   P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range
"""


def new_range(start=0, stop=0, step=1):
    if start > 0 and stop == 0:
        stop = start
        start = 0
    elif step == 0:
        raise ValueError("range() arg 3 must not be zero")
    elif start > 0 and stop > 0 and start > stop:
        return

    i = start
    if start < stop and step != 0:
        while i < stop:
            yield i
            i += step
    elif start > stop:
        while i > stop:
            yield i
            i += step


for i in new_range(10):
    print(i)
