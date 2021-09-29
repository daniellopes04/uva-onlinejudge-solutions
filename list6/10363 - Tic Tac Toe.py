# -*- coding: UTF-8 -*-
def lost(grid, character):
    if (grid[0][0] == character and grid[0][1] == character and grid[0][2] == character):
        return False
    
    if (grid[1][0] == character and grid[1][1] == character and grid[1][2] == character):
        return False
        
    if (grid[2][0] == character and grid[2][1] == character and grid[2][2] == character):
        return False
        
    if (grid[0][0] == character and grid[1][0] == character and grid[2][0] == character):
        return False
    
    if (grid[0][1] == character and grid[1][1] == character and grid[2][1] == character):
        return False
        
    if (grid[0][2] == character and grid[1][2] == character and grid[2][2] == character):
        return False
        
    if (grid[0][0] == character and grid[1][1] == character and grid[2][2] == character):
        return False
        
    if (grid[0][2] == character and grid[1][1] == character and grid[2][0] == character):
        return False
    
    return True

def main():
    cases = int(input())

    for i in range(cases):
        grid = []
        countX = 0
        countO = 0

        if (i != 0):
            aux = input()

        for _ in range(3):
            line = input()
            
            countX += line.count('X')
            countO += line.count('O')

            grid.append(list(line))

        if (countX == countO):
            valid = lost(grid, 'X')
        elif (countX == countO + 1):
            valid = lost(grid, 'O')
        else:
            valid = False

        if (valid):
            print('yes')
        else:
            print('no')

if __name__=='__main__':
	main()
