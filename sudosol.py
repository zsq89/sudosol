'''
sudosol - A sudoku solver powered by backtracking algorithm
sudosol reads in the puzzle in puzzle.txt, 
and print the well formatted solution in stdout
'''

import sys

P_SIZE = 9  # puzzle size
G_SIZE = 3  # grid size

# print puzzle in a pretty format
def printPuzzle(p):
    for i in range(P_SIZE):
        for j in range(P_SIZE):
            if p[i][j] > 0:
                print(' ' + str(p[i][j]) + ' ', end = '  ')
            else:
                print(' ~ ', end = '  ')
            if j % G_SIZE == 2:
                print('', end = '  ')
        print('\n')
        if i % G_SIZE == 2:
            print('\n')
    pass

# find the first to-be-filled cell of the puzzle
def findFirstDefect(p):
    for i in range(P_SIZE):
        for j in range(P_SIZE):
            if p[i][j] == 0:
                return (i, j)
    return None
    pass

# check if a number is valid at a cell of the puzzle
def isCollision(p, x, y, n):
    if p[x][y] > 0:
        return True
    for i in range(P_SIZE):
        if p[x][i] == n and i != y:
            return True
    for j in range(P_SIZE):
        if p[j][y] == n and j != x:
            return True
    rx = int(x / G_SIZE)
    ry = int(y / G_SIZE)
    for i in range(rx * G_SIZE, (rx + 1) * G_SIZE):
        for j in range(ry * G_SIZE, (ry + 1) * G_SIZE):
            if p[i][j] == n and (i != x or j != y):
                return True
    return False
    pass

# solve the puzzle
def solveSudoku(p):
    d = findFirstDefect(p)
    if not d:
        return p
    else:
        for n in range(1, P_SIZE + 1):
            if not isCollision(p, d[0], d[1], n):
                p[d[0]][d[1]] = n
#                 print(p)
                if solveSudoku(p):
                    return p
                else:
                    p[d[0]][d[1]] = 0
    return None
    pass

def main():
    with open('puzzle.txt', 'r') as f:
        p = []
        for line in f:
            row = [int(n) if n != '-' else 0 for n in line.split()]
            p.append(row)
    print('Puzzle loaded:\n')
    printPuzzle(p)
    print('\n')
    s = solveSudoku(p)
    if s != None:
        print("Puzzle solved:\n")
        printPuzzle(s)
    else:
        print("No solution!")
    pass

if __name__ == '__main__':
    sys.exit(main())