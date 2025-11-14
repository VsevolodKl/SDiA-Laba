def bead_sort(arr):
    """
    Сортировка бусинами - визуализирует сортировку как падающие бусины
    Работает только с неотрицательными целыми числами
    """
    if len(arr) == 0:
        return arr
    
    # Шаг 1: Находим максимальное значение
    max_val = max(arr)
    
    # Шаг 2: Создаем "стержни" с бусинами
    # Каждый стержень представляет один элемент массива
    beads = [[1] * num + [0] * (max_val - num) for num in arr]
    
    # Шаг 3: "Заставляем бусины падать" - транспонируем матрицу
    for i in range(max_val):
        for j in range(len(arr)):
            # Подсчитываем количество бусин в каждом столбце
            beads[j][i] = 1 if i < arr[j] else 0
    
    # Шаг 4: Подсчитываем бусины в каждом стержне после "падения"
    result = []
    for i in range(max_val):
        count = 0
        for j in range(len(arr)):
            count += beads[j][i]
        result.append(count)
    
    # Шаг 5: Преобразуем обратно в отсортированный массив
    # Более эффективная реализация "падения бусин":
    for i in range(len(arr)):
        for j in range(max_val - 1, -1, -1):
            if beads[i][j] == 1:
                arr[i] = j + 1
                break
    
    return sorted(arr)  # Возвращаем отсортированную копию

# Альтернативная, более эффективная реализация
def bead_sort_optimized(arr):
    """Оптимизированная версия сортировки бусинами"""
    if not arr:
        return []
    
    max_val = max(arr)
    
    # Создаем матрицу бусин
    beads = [[0] * max_val for _ in range(len(arr))]
    
    # Расставляем бусины
    for i, num in enumerate(arr):
        for j in range(num):
            beads[i][j] = 1
    
    # "Заставляем бусины падать"
    for j in range(max_val):
        sum_beads = 0
        for i in range(len(arr)):
            sum_beads += beads[i][j]
            beads[i][j] = 0
        
        # Размещаем бусины внизу
        for i in range(len(arr) - 1, len(arr) - sum_beads - 1, -1):
            beads[i][j] = 1
    
    # Преобразуем обратно в числа
    result = [sum(row) for row in beads]
    return result

# Пример использования
arr = [3, 1, 4, 1, 5, 9, 2, 6]
print("Исходный массив:", arr)
print("Отсортированный массив:", bead_sort_optimized(arr))