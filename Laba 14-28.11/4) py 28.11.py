#Вариант 11

def generate_permutations(s: str) -> list[str]:
    """
    Генерирует все уникальные перестановки строки.
    
    >>> sorted(generate_permutations("ab"))
    ['ab', 'ba']
    >>> sorted(generate_permutations("abc"))
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    """
    # Базовый случай: строка из одного символа или пустая строка
    if len(s) <= 1:
        return [s]
    
    permutations = []
    
    # Итерируем по каждому символу, делая его первым элементом перестановки
    for i in range(len(s)):
        # Текущий символ (становится префиксом)
        current_char = s[i]
        
        # Оставшаяся часть строки
        remaining_chars = s[:i] + s[i+1:]
        
        # Рекурсивно получаем перестановки оставшейся части
        sub_permutations = generate_permutations(remaining_chars)
        
        # Добавляем текущий символ в начало каждой под-перестановки
        for sub_perm in sub_permutations:
            permutations.append(current_char + sub_perm)
            
    return permutations