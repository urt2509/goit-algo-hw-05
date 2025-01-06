import re
from collections.abc import Callable


def generator_numbers(text: str):
    pattern = r"(\d+.\d+)"
    text_lst = re.findall(pattern, text)

    for i in text_lst:
        yield i


def sum_profit(text: str, func: Callable):
    sum_total = 0
    for i in generator_numbers(text):
        i = float(i)
        sum_total = sum_total + i

    return sum_total
