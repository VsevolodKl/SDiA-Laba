def bucket_sort(arr):
    """
    Блочная сортировка - распределяет элементы по "корзинам", 
    затем сортирует каждую корзину отдельно
    """
    if len(arr) == 0:
        return arr
    
    # Шаг 1: Находим минимальное и максимальное значение
    min_val = min(arr)
    max_val = max(arr)
    
    # Шаг 2: Создаем пустые корзины
    bucket_count = len(arr)  # Количество корзин = количеству элементов
    buckets = [[] for _ in range(bucket_count)]
    
    # Шаг 3: Распределяем элементы по корзинам
    for num in arr:
        # Вычисляем индекс корзины для текущего числа
        index = int((num - min_val) / (max_val - min_val) * (bucket_count - 1))
        buckets[index].append(num)
    
    # Шаг 4: Сортируем каждую корзину (используем встроенную сортировку)
    for bucket in buckets:
        bucket.sort()
    
    # Шаг 5: Объединяем отсортированные корзины
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)
    
    return sorted_arr

# Пример использования
arr = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
print("Исходный массив:", arr)
print("Отсортированный массив:", bucket_sort(arr))