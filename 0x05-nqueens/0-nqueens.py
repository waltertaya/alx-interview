#!/usr/bin/python3
""" N queens """
import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])


def queens(n, i=0, a=[], b=[], c=[]):
    '''
    n: size of the board
    i: current row
    a: columns occupied
    b: diagonals occupied
    c: other diagonals occupied
    '''
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def solve_nqueens(n):
    ''' solve_nqueens the N queens problem
      n: size of the board
    '''
    k = []
    i = 0
    for solution in queens(n, 0):
        for s in solution:
            k.append([i, s])
            i += 1
        print(k)
        k = []
        i = 0


solve_nqueens(n)
