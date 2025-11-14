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

# Примеры использования


print("\n" + "="*50)
print("=== Пример 1: Эффективность на большом массиве ===")
import time

# Создаем большой отсортированный массив
large_arr = list(range(1, 1000001))  # 1 до 1,000,000
target3 = 543210

start_time = time.time()
result3 = exponential_search(large_arr, target3)
end_time = time.time()

print(f"Поиск элемента {target3} в массиве из 1,000,000 элементов")
print(f"Результат: {result3}")
print(f"Время выполнения: {(end_time - start_time)*1000:.4f} мс")