# Вариант 2
def power(x: float, n: int) -> float:
    """
    Вычисляет x в степени n рекурсивно.
    
    >>> power(2, 4)
    16.0
    >>> power(3, 3)
    27.0
    >>> power(2, -2)
    0.25
    """
    if n == 0:
        # Базовый случай: x^0 = 1
        return 1.0
    
    if n < 0:
        # Обработка отрицательной степени: x^(-n) = 1 / x^n
        return 1.0 / power(x, -n)
    
    # Рекурсивный шаг (быстрое возведение в степень)
    if n % 2 == 0:
        # Если n четное: x^n = (x^(n/2))^2
        half_power = power(x, n // 2)
        return half_power * half_power
    else:
        # Если n нечетное: x^n = x * (x^((n-1)/2))^2
        half_power = power(x, (n - 1) // 2)
        return x * half_power * half_power