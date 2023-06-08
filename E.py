"""
ЗАДАНИЕ:
Написать класс, принимающий на вход текст.
Один метод класса должен выводить в консоль самое длинное слово в тексте.
Второй метод - самое часто встречающееся слово.
Третий метод выводит количество спецсимволов в тексте (точки, запятые и так далее).
Четвертый метод выводит все палиндромы через запятую.
"""
import string
from operator import itemgetter
from typing import Optional
from F import my_decorator


MAIN_TEXT = """o4en  ogo ogo топот dlinnoe , , , , o4en predlojenie"""


@my_decorator
class TextClass:  # (metaclass=TimeClass):

    """
    Класс для работы со строками.
    """

    def __init__(self, text: str) -> None:
        self.text = str(text).lower()
        self.punctuation = string.punctuation

    def __max_entry(self, text: str, text_2: Optional[str] = None) -> tuple:
        """
        Функция возвращает ключ словаря с максимальным значением значения.
        Если таких ключей несколько, вернет рандомное вхождение.
        """
        text_2 = text_2 if text_2 is not None else text
        return max(
            {word: text.count(word) for word in set(text_2)}.items(), key=itemgetter(1)
        )

    def __remove_punctuation(self, text) -> str:
        """
        Функция удаляет различные знаки из текста.
        """
        return text.translate(str.maketrans("", "", self.punctuation)).split()

    def max_len(self) -> str:
        """
        Функция возвращает самое длинное слово.
        """
        return f'Самое длинное слово: "{max(self.text.split())}"'

    def most_freq(self) -> str:
        """
        Функция возвращает самое встречающееся слово из строки.
        """
        edited_text = self.__remove_punctuation(self.text)
        freq_word = self.__max_entry(edited_text)
        return f'Слово: "{freq_word[0]}". Встречается: {freq_word[1]} раз(a)'

    def count_chars(self) -> str:
        """
        Функция возвращает самый встречающийся спецсимвол.
        """
        freq_char = self.__max_entry(self.text, self.punctuation)
        return f'Символ: "{freq_char[0]}". Встречается: {freq_char[1]} раз(a)'

    def palindrom(self) -> str:
        """
        Функция выводит уникальные палиндромы через запятую.
        """
        words = self.__remove_punctuation(self.text)
        return f'Уникальные палиндромы: {", ".join(set([word for word in words if word == word[::-1]]))}'


txt_cls = TextClass(MAIN_TEXT)

print(txt_cls.max_len())
print(txt_cls.most_freq())
print(txt_cls.count_chars())
print(txt_cls.palindrom())
