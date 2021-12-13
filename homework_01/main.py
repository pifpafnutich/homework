"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*items):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    
    return [ item*item for item in items ]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number):
    """
    функция, которая проверяет, является ли число простым.
    можно сделать декоратор, который собирает простые числа,
    который постепенно складывает простые числа в кэш, после
    чего каждый следующий запуск уже сравнивает с числами
    из кэша, а затем уже на следующие числа.
    
    Для единичного числа можно 
    """
    for i in range(2,number):
        if number % i == 0:
            return False
    return True    


def filter_numbers(nums, type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if type == EVEN:
        return list(filter(lambda num: num % 2 == 0, nums))    
    if type == ODD:
        return list(filter(lambda num: num % 2 != 0, nums))
    if type == PRIME:
        return list(filter(is_prime, nums))