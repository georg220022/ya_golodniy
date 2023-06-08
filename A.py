"""
ЗАДАНИЕ:
    Функция принимает в качестве аргумента набор ссылок. Ссылки имеют формат ссылок на проекты на гитхабе
    (например: https://github.com/miguelgrinberg/Flask-SocketIO, https://github.com/miguelgrinberg/Flask-SocketIO.git).
    Функция должна обработать полученные ссылки и вывести в консоль названия самих гит-проектов.
    Стоит рассмотреть защиту от ссылок "вне формата".
"""
import re

# from F import TimeClass


MAIN_URL = "github.com/"
BAD_MSG = "Не валидный урл или не содержит названия, номер в списке: "
MIN_LEN_NAME = 1
MAX_LEN_NAME = 100
BAD_FIRST_SYMBOL_IN_NAME = "."
REG = r"github\.com\/\w+\/([\w.-]+)"  # Спасибо ChatGPT за регулярку =)

repo_list = [
    "http://github.com/georg220022/.wfeearg/",  # 1
    "http://github.com/georg220022/wefefg./",  # 2
    "http://github.com/georg220022/ /not_valid",  # 3
    "http://github.com/georg220022/qc///",  # 4
    "http://github.com/georg220022/ASDcqs/SDFffff1/1FDWE",  # 5
    "http://github.com/georg220022/***/wefcww",  # 6
    "http://github.com/georg220022/-/fewf2f",  # 7
    "http://github.com/georg220022/_-_-_/12rewefe3",  # 8
    "https://github.com/georg220022/restaurant_menu_api/123123rwqef",  # 9
    "http://github.com/georg220022/resta-u.rant_menu_api/ewfwef",  # 10
    "https://www.github.com/georg220022/restaurant_menu_api",  # 11
    "http://www.github.com/georg220022/restaura...nt_menu_api",  # 12
    "github.com/georg220022/restaurant_menu_api1",  # 13
    "pornhub.com/georg220022/restaurant_menu_api",  # 14
    "",  # 15
    "2345678",  # 16
    "github.com/",  # 17
]


def get_name_repo(repo_list: list) -> None:
    """
    Вытаскиваем имя репы из строки
    """
    for id_, link in enumerate(repo_list):
        if isinstance(link, str):
            if match := re.search(REG, link):
                result = match.group(1)
                """
                1) Имя репы может содержать точку но не начинаться с нее.
                2) Максимальная длинна имени репы 100 символов (минимальная 1)
                """
                if (
                    len(result) == len(result.replace(" ", ""))
                    and MIN_LEN_NAME <= len(result) <= MAX_LEN_NAME
                    and result[0] != BAD_FIRST_SYMBOL_IN_NAME
                ):
                    print(result)
                    continue
        print(BAD_MSG, id_ + 1)

get_name_repo(repo_list)
