# Write your code here :-)
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
grid_size = len(grid)

for i in range(6): #loops each grid item [0-8][0-5]
    for k in range(grid_size):
        if k == grid_size - 1:
            print(grid[k][i], end='\n')
        else:
            print(grid[k][i], end='')
