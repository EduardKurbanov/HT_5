"""
7. Реалізуйте генератор, який приймає на вхід будь-яку ітерабельну послідовність (рядок, список, кортеж) і повертає генератор,
який буде вертати значення з цієї послідовності, при цьому, якщо було повернено останній елемент із послідовності - ітерація починається знову.

   Приклад (якщо запустили його у себе - натисніть Ctrl+C ;) ):

   # >>>for elem in generator([1, 2, 3]):

   ...    print(elem)

   ...

   1\n 2\n 3\n 1\n 2\n 3\n 1\n
   .......
"""
import time

def generator(*args):
    while True:
        for i in iter(*args):
            yield i
            time.sleep(0.5)


while True:
    try:
        str_1 = "12345645g"
        list_1 = [1, 2, 3, 4, 5, 6, "45g"]
        tuple_1 = (1, 2, 3, 4, 5, 6, "45g")

        for i in generator(tuple_1):
            print(i)

        print("*" * 60)
        yes = input('if you want to leave the program press "Y" if not then "N": ')
        print("*" * 60)
        if "y" == yes.lower():
            break
        else:
            continue
    except Exception as err:
        print("<<error>> {0}".format(err))
