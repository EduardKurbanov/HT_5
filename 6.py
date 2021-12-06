"""
6. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.

   P.S. Повинен вертатись генератор.

   P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range
"""


def new_range(start=None, stop=None, step=None):
    if (type(start).__name__ and type(stop).__name__ and type(step).__name__) != 'int':
        if type(start).__name__ != 'int':
            if type(start).__name__ == 'NoneType':
                raise TypeError("range expected at least 1 argument, got 0")
            else:
                raise TypeError("'{0}' object cannot be interpreted as an integer".format(type(start).__name__))
        elif type(stop).__name__ != 'int' and type(stop).__name__ != 'NoneType':
            raise TypeError("'{0}' object cannot be interpreted as an integer".format(type(stop).__name__))
        elif type(step).__name__ != 'int' and type(step).__name__ != 'NoneType':
            raise TypeError("'{0}' object cannot be interpreted as an integer".format(type(step).__name__))

    new_start = int(start)
    if stop is None:
        new_stop = 0
    else:
        new_stop = int(stop)

    if step is None:
        new_step = 0
    else:
        new_step = int(step)

    if new_start > 0 and stop is None and step is None:
        new_stop = new_start
        new_start = 0
        new_step = 1
    elif new_start < 0 and stop is None and step is None:
        return
    elif (new_start <= 0 or new_start >= 0) and new_stop > new_start and step is None:
        new_step = 1
    elif new_start < 0 and new_start < new_stop and (new_stop <= 0 or new_stop >= 0) and new_step <= 0:
        return
    elif new_start > 0 and new_start < new_stop and new_step <= 0:
        return
    elif new_start < 0 and new_stop < 0 and new_step >= 0:
        return
    elif new_start > 0 and new_stop < 0 and new_step >= 0:
        return
    elif new_step == 0:  # or new_step < 0:
        if new_step == 0:
            raise ValueError("range() arg 3 must not be zero")
        else:
            return

    i = new_start
    if new_start < new_stop and new_step != 0:
        while i < new_stop:
            yield i
            i += new_step
    elif new_start > new_stop:
        while i > new_stop:
            yield i
            i += new_step


for i in new_range(10):
    print(i, end=" ")
print("*" * 30 + "new_range(10)")

for i in new_range(1, 11):
    print(i, end=" ")
print("*" * 30 + "new_range(1, 11)")

for i in new_range(0, -10, -1):
    print(i, end=" ")
print("*" * 30 + "new_range(0, -10, -1)")

for i in new_range(10, 2, -2):
    print(i, end=" ")
print("*" * 30 + "new_range(10, 2, -2)")

for i in new_range(10, -2, -2):
    print(i, end=" ")
print("*" * 30 + "new_range(10, -2, -2)")

for i in new_range(-10, 2, 2):
    print(i, end=" ")
print("*" * 30 + "new_range(-10, 2, 2)")

for i in new_range(-10, -2, -2):
    print(i, end=" ")
print("*" * 30 + "new_range(-10, -2, -2)")

for i in new_range(-10, -20, -2):
    print(i, end=" ")
print("*" * 30 + "new_range(-10, -20, -2)")

for i in new_range(10, -20, -2):
    print(i, end=" ")
print("*" * 30 + "new_range(10, -20, -2)")

for i in new_range(-10, 20, 2):
    print(i, end=" ")
print("*" * 30 + "new_range(-10, 20, 2)")

for i in new_range(-10, -20, 2):
    print(i, end=" ")
print("*" * 30 + "new_range(-10, -20, 2)")
#
for i in new_range(10, -20, 2):
    print(i, end=" ")
print("*" * 30 + "new_range(10, -20, 2)")
