from typing import Union
"""
Импортировал модуль Union, для корректного интерпретированная, что параметр a и b принимают разные типы данных как 
целые числа, числа с плавающей точкой и строки. В случае отсутствия данного модуля интерпретатор ожидал бы список из
разных типов данных. В случае передачи параметров a и b списком, то необходимость в данном модуле отсутствовала.
Тогда функция имела бы вид def add_everything_up(a, b)
"""

def add_everything_up(a: Union[int, float, str], b: Union[int, float, str]):
    try:
        c = a + b
        print(f'Результат сложения: {round(c,3)}')
        return round(c,3)
    except TypeError:
        c = f'{a}{b}'
        return c

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))