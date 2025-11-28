#Вариант 7

from typing import Union

def find_max_recursive(arr: list) -> Union[int, float]:
    """
    Находит максимальный элемент в списке (массиве) рекурсивно.
    
    >>> find_max_recursive([1, 5, 2, 9, 3])
    9
    >>> find_max_recursive([-10, -1, -5.5])
    -1
    """
    # 1. Обработка исключения (если на вход подали пустой список)
    if not arr:
        # В этом случае функция не возвращает ни int, ни float, 
        # а выбрасывает исключение.
        raise ValueError("Нельзя найти максимальный элемент в пустом массиве.")
    
    # 2. Базовый случай: массив из одного элемента
    if len(arr) == 1:
        return arr[0]
    
    # 3. Рекурсивный шаг:
    max_of_rest = find_max_recursive(arr[1:])
    
    # Возвращаем больший из двух элементов
    return arr[0] if arr[0] > max_of_rest else max_of_rest