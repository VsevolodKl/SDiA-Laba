#Вариант 16


# root = [значение, левое_поддерево, правое_поддерево]

def preorder_traversal_list(root: list or None) -> list:
    """
    Обход "корень -> левое поддерево -> правое поддерево".
    """
    result = []
    if root:
        value = root[0]
        left_subtree = root[1]
        right_subtree = root[2]
        
        # 1. Корень
        result.append(value)      
        # 2. Левое поддерево
        result.extend(preorder_traversal_list(left_subtree))  
        # 3. Правое поддерево
        result.extend(preorder_traversal_list(right_subtree)) 
        
    return result

def inorder_traversal_list(root: list or None) -> list:
    """
    Обход "левое поддерево -> корень -> правое поддерево".
    """
    result = []
    if root:
        value = root[0]
        left_subtree = root[1]
        right_subtree = root[2]
        
        # 1. Левое поддерево
        result.extend(inorder_traversal_list(left_subtree))   
        # 2. Корень
        result.append(value)      
        # 3. Правое поддерево
        result.extend(inorder_traversal_list(right_subtree))  
        
    return result

def postorder_traversal_list(root: list or None) -> list:
    """
    Обход "левое поддерево -> правое поддерево -> корень".
    """
    result = []
    if root:
        value = root[0]
        left_subtree = root[1]
        right_subtree = root[2]
        
        # 1. Левое поддерево
        result.extend(postorder_traversal_list(left_subtree))  
        # 2. Правое поддерево
        result.extend(postorder_traversal_list(right_subtree)) 
        # 3. Корень
        result.append(value)      
        
    return result