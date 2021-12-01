"""
2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:

   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;

   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;

   - пароль повинен мати хоча б один символ із цих - @$#%&?!

   Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.
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

while True:
        print("*" * 76)
        print("<<name / password pair validation. >>")
        print("<<login must be less than 3 characters no more than 50. >>")
        print("<<password must be greater than 8 have at least one digit and a '@$#%&?!'. >>")
        print("*" * 76)
        login = input("login: ")
        password = input("password: ")

        val_log_pass(login, password)

        print("*" * 60)
        yes = input('if you want to leave the program press "Y" if not then "N": ')
        print("*" * 60)
        if "y" == yes.lower():
            break
        else:
            continue


