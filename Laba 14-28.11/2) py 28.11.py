#Вариант 4

def reverse_string(s: str) -> str:
    """
    Переворачивает строку рекурсивно.
    
    >>> reverse_string("hello")
    'olleh'
    >>> reverse_string("python")
    'nohtyp'
    """
    # Базовый случай: пустая строка или строка из одного символа
    if len(s) <= 1:
        return s
    
    # Рекурсивный шаг: s[0] + reverse_string(s[1:])
    # Ошибка в логике, должно быть: reverse_string(s[1:]) + s[0]
    # Берем последний символ и добавляем к перевернутой оставшейся части
    return reverse_string(s[1:]) + s[0]