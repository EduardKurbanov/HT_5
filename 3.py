"""
3. На основі попередньої функції створити наступний кусок кода:

   а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;

   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором,
        перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:

      Name: vasya

      Password: wasd

      Status: password must have at least one digit

      -----

      Name: vasya

      Password: vasyapupkin2000

      Status: OK

   P.S. Не забудьте використати блок try/except ;)
"""

import re


class LoginException(Exception):
    pass


class PasswordException(Exception):
    pass


class SymbolException(Exception):
    pass


def val_log_pass(login, password):
    """
    :param login: -> must be not less than 3 characters and not more than 50.
    :param password: -> the password must be at least 8 characters and must have at least one digit and a '@$#%&?!'.
    :return True or Exception.
    """

    print("Name: {0}".format(login))
    print("Password: {0}".format(password))

    try:
        if len(str(login)) > 3 and len(str(login)) < 50:
            if len(str(password)) < 8:
                raise PasswordException(f"password must be more than 8 characters-> {password}")

            elif re.search(r'[0-9]', str(password)) and re.search(r'[@$#%&?!]', password) and (
                    re.search(r'[a-z]', password) or re.search(r'[A-Z]]', password)):
                print("Status: OK")

            elif re.search(r'[@$#%&?!]', password) == None:
                raise SymbolException(f"there must be at least one character '@$#%&?!' -> {password}")

            elif re.search(r'[0-9]', str(password)) == None:
                raise PasswordException(f"password must be more than 8 and at least one digit '0-9' -> {password}")

            else:
                raise PasswordException(f"password must be more than 8 and at least one or more letters 'a-z' 'A-Z'-> {password}")

        else:
            raise LoginException(f"Login must be not less than 3 characters and not more than 50 -> {login}")

    except LoginException as err:
        print("Status: {0}".format(err))
    except PasswordException as err:
        print("Status: {0}".format(err))
    except SymbolException as err:
        print("Status: {0}".format(err))


log_pass_list1 = [
    ["Anton", "123qwe1#@"],
    ["Bob", "qweqwr6548"],
    ["Tom", "7895465#?"],
    ["Ed", "987poi4%"],
    ["Sam", "12345qwe%$"],
    ["Vasja", "assa####z"],
    ["Rahul", "ADS222312"],
    ["Petro", "AsS#22"],
]

while True:

    for k, v in log_pass_list1:
        val_log_pass(str(k), str(v))

    print("*" * 60)
    yes = input('if you want to leave the program press "Y" if not then "N": ')
    print("*" * 60)
    if "y" == yes.lower():
        break
    else:
        continue

