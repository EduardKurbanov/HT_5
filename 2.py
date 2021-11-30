"""
2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:

   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;

   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;

   - пароль повинен мати хоча б один символ із цих - @$#%&?!

   Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.
"""
import re


def val_log_pass(login, password):
    """
    :param login: -> must be not less than 3 characters and not more than 50.
    :param password: -> the password must be at least 8 characters and must have at least one digit and a '@$#%&?!'.
    :return True or Exception.
    """

    if len(str(login)) >= 3 and len(str(login)) <= 50:
        if len(str(password)) >= 8 and (re.search('[0-9]', str(password))):
            if re.search('[@$#%&?!]', password):
                print("login and pass -> OK")
            else:
                raise Exception("SymbolException")
        else:
            raise Exception("PasswordException")
    else:
        raise Exception("LoginException")


while True:
    try:
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
    except Exception as err:
        print("<<error>> {0}".format(err))
