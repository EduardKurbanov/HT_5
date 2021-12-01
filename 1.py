"""
1. Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
   Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>)
            і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).

   Логіка наступна:

       якщо введено коректну пару ім'я/пароль - вертається <True>;

       якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>,
            інакше (<silent> == <False>) - породжується виключення LoginException
"""


class LoginException(Exception):
    pass


def verification_password_login(username, password, silent=False):
    log_pass_list = [
        ["Anton", "123qwe1"],
        ["Bob", "456rty2"],
        ["Tom", "789uio3"],
        ["Ed", "987poi4"],
        ["Sam", "654asd5"]
    ]
    dict_lis = dict(log_pass_list)

    if (username, password) in dict_lis.items():
        return True
    elif ((username, password) not in dict_lis.items()) and (silent == True):
        return False
    elif silent == False:
        raise LoginException(f"invalid login: -> {username}")


while True:
    try:
        login = input("enter login: ")
        password = input("enter pass: ")
        silent = input("enter true or false: ")

        if login and password and silent:
            print(verification_password_login(str(login), str(password), bool(silent)))
        elif login and password:
            print(verification_password_login(login, password))

        print("*" * 60)
        yes = input('if you want to leave the program press "Y" if not then "N": ')
        print("*" * 60)
        if "y" == yes.lower():
            break
        else:
            continue
    except LoginException as err:
        print(err)
