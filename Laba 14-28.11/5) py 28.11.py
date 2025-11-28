#Вариант 15

def find_all_maze_paths(maze_size: int = 5):
    """
    Генерирует все возможные пути из (0, 0) в (maze_size-1, maze_size-1)
    в лабиринте размера maze_size x maze_size, где 0 - проходимо, 1 - стена.
    
    Для простоты, лабиринт по умолчанию проходим (только 0).
    """
    maze = [[0] * maze_size for _ in range(maze_size)]
    start = (0, 0)
    end = (maze_size - 1, maze_size - 1)
    all_paths = []

    def solve_maze_util(r, c, path):
        # r - текущая строка, c - текущий столбец

        # 1. Проверка на выход за границы или стену
        if r < 0 or r >= maze_size or c < 0 or c >= maze_size or maze[r][c] == 1:
            return

        # 2. Проверка на посещение (для избежания циклов)
        if (r, c) in path:
            return
        
        # Добавляем текущую позицию в путь
        path.append((r, c))

        # 3. Базовый случай: Достигнута конечная точка
        if r == end[0] and c == end[1]:
            # Найден полный путь, добавляем его копию
            all_paths.append(list(path))
            
            # Важно: нужно продолжить поиск с возвратом для рассмотрения других путей
            path.pop() # Откат
            return

        # 4. Рекурсивный шаг: Попытка двигаться в 4 направлениях (вправо, влево, вниз, вверх)
        
        # Вправо
        solve_maze_util(r, c + 1, path)
        # Вниз
        solve_maze_util(r + 1, c, path)
        # Влево
        solve_maze_util(r, c - 1, path)
        # Вверх
        solve_maze_util(r - 1, c, path)

        # 5. Откат (Backtracking): Удаляем текущую позицию из пути, 
        # чтобы попробовать другие варианты из предыдущей ячейки
        path.pop()

    # Запуск поиска из начальной точки
    solve_maze_util(start[0], start[1], [])
    return all_paths

# Пример использования: (может быть очень много путей в 5x5 полностью открытом лабиринте!)
# paths = find_all_maze_paths(3) # Пример для 3x3, чтобы не перегружать вывод
# print(f"Найдено путей в лабиринте 3x3: {len(paths)}")