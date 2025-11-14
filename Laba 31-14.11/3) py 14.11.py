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

# Пример использования
arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
target = 55
print(f"Массив: {arr}")
print(f"Поиск элемента {target}")
result = jump_search(arr, target)
if result != -1:
    print(f"Элемент найден на позиции {result}")
else:
    print("Элемент не найден")