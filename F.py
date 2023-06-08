"""
ЗАДАНИЕ:
    Написать декоратор к предыдущему классу, который будет выводить в консоль время выполнения каждого метода.
    Результат выполнения задания должен быть оформлен в виде файла с кодом.
"""
import time

IGNORE_METHODS = ("_TextClass__max_entry", "_TextClass__remove_punctuation", "__init__")


def my_decorator(cls):
    class DecoratedClass(cls):
        def __getattribute__(self, name):
            attribute = super().__getattribute__(name)
            if callable(attribute) and name not in IGNORE_METHODS:

                def wrapped(*args, **kwargs):
                    start_time = time.perf_counter()
                    result = attribute(*args, **kwargs)
                    end_time = time.perf_counter()
                    run_time = end_time - start_time
                    print(f"\nВремя работы {name}: {run_time:.7f}")
                    return result

                return wrapped
            return attribute

    return DecoratedClass


'''
Написал эту дичь, а потом понял что лучше декоратором а не метаклассом :'C 
а удалять жалко



from functools import wraps
from typing import Any, Callable, DefaultDict, Optional, Sequence, Type, TypeVar

T = TypeVar("T", bound="TimeClass")


class TimeClass(type):
    """
    Класс 'декоратор'.
    Замеряет время работы всех методов кроме методов из кортежа 'IGNORE_METHODS'.
    Можно использовать как отдельный декоратор для функций (@TimeClass.time_it) или
    как декоратор методов класса через metaclass=TimeClass
    """

    def __new__(cls: Type[T], name: str, bases: tuple, dct: dict) -> T:
        for attr_name in dct:
            attr_value = dct[attr_name]
            if callable(attr_value) and attr_name not in IGNORE_METHODS:
                dct[attr_name] = cls.time_it(attr_value)
        return super().__new__(cls, name, bases, dct)

    @staticmethod
    def time_it(func: Callable) -> Callable:
        """
        Добавим @staticmethod + @wraps для возможности импортирования этой функции как
        декоратора отдельно и не трерять информацию о декорируемой функции
        """
        @wraps(func)
        def wrapper(*args: Sequence, **kwargs: DefaultDict) -> Optional[Any]:
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            run_time = end_time - start_time
            print(f"\nМетод '{func.__name__}' отработал за {run_time:.7f} сек")
            return result

        return wrapper
'''
