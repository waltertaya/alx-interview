#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    
    Parameters:
    boxes (list of list of int): A list of boxes, each containing a list of keys.

    Returns:
    bool: True if all boxes can be opened, else False.
    """
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    stack = [0]
    
    while stack:
        current_box = stack.pop()
        
        for key in boxes[current_box]:
            if key < n and not opened[key]:
                opened[key] = True
                stack.append(key)
    
    return all(opened)

