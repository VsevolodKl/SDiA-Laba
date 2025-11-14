import math

def jump_search(arr, target):
    """
    Поиск скачками - прыгает с фиксированным шагом, затем делает линейный поиск
    Требует отсортированный массив
    """
    n = len(arr)
    
    # Шаг 1: Определяем размер прыжка (квадратный корень из длины)
    step = int(math.sqrt(n))
    
    # Шаг 2: Находим блок, где может находиться элемент
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1  # Элемент не найден
    
    # Шаг 3: Линейный поиск в найденном блоке
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1  # Элемент не найден
    
    # Шаг 4: Проверяем, найден ли элемент
    if arr[prev] == target:
        return prev
    else:
        return -1

def ternary_search(arr, target):
    """
    Тернарный поиск - делит массив на три части
    Рекурсивная реализация
    """
    def ternary_recursive(left, right):
        if left > right:
            return -1
        
        # Шаг 1: Делим массив на три части
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        # Шаг 2: Проверяем точки деления
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
        
        # Шаг 3: Определяем, в какой части продолжать поиск
        if target < arr[mid1]:
            return ternary_recursive(left, mid1 - 1)
        elif target > arr[mid2]:
            return ternary_recursive(mid2 + 1, right)
        else:
            return ternary_recursive(mid1 + 1, mid2 - 1)
    
    return ternary_recursive(0, len(arr) - 1)

def ternary_search_iterative(arr, target):
    """
    Тернарный поиск - итеративная реализация
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        # Шаг 1: Делим массив на три части
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        # Шаг 2: Проверяем точки деления
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
        
        # Шаг 3: Определяем, в какой части продолжать поиск
        if target < arr[mid1]:
            right = mid1 - 1
        elif target > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
    
    return -1


def exponential_search(arr, target):
    """
    Экспоненциальный поиск - состоит из двух этапов:
    1. Нахождение диапазона экспоненциальным увеличением границ
    2. Бинарный поиск в найденном диапазоне
    Особенно эффективен для неограниченных массивов
    """
    
    def binary_search(arr, left, right, target):
        """Вспомогательная функция бинарного поиска"""
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    n = len(arr)
    
    # Шаг 1: Проверка пустого массива и первого элемента
    if n == 0:
        return -1
    
    if arr[0] == target:
        return 0
    
    # Шаг 2: Экспоненциальное увеличение границы
    i = 1
    while i < n and arr[i] <= target:
        i *= 2  # Увеличиваем в 2 раза на каждом шаге
    
    # Шаг 3: Бинарный поиск в найденном диапазоне
    left = i // 2  # Начало диапазона
    right = min(i, n - 1)  # Конец диапазона (не превышаем длину массива)
    
    return binary_search(arr, left, right, target)


def compare_search_algorithms():
    """Сравнение различных алгоритмов поиска"""
    import time
    
    # Создаем тестовый массив
    arr = list(range(1, 1000001))  # 1 до 1,000,000
    target = 54321
    
    algorithms = {
        "Jump Search": jump_search,
        "Exponential Search": exponential_search,
        "Ternary Search": ternary_search_iterative
    }
    
    print("Сравнение алгоритмов поиска:")
    print(f"Размер массива: {len(arr):,}")
    print(f"Целевой элемент: {target}")
    print()
    
    for name, algorithm in algorithms.items():
        start_time = time.time()
        result = algorithm(arr, target)
        end_time = time.time()
        
        print(f"{name}:")
        print(f"  Позиция: {result}")
        print(f"  Время: {(end_time - start_time)*1000:.4f} мс")
        print()

# Запуск сравнения
compare_search_algorithms()