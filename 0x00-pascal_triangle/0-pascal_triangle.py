#!/usr/bin/python3
'''
0-pascal_triangle
'''
def pascal_triangle(n):
    '''
    returns a list of lists of integers representing the Pascal’s triangle of n
    '''
    pascal_list = [[1]]
    temp = [0, 1, 0]
    if n <= 0:
        return []
    for i in range(0, n):
        my_list = []
        for j in temp:
            if (temp[j + 1] == temp[-1]):
                break
            my_list.append((temp[j] + temp[j + 1]))
        pascal_list.append(my_list)
        temp = pascal_list[i]
        temp.insert(0, 0)
        temp.insert(-1, 0)
    return pascal_list
