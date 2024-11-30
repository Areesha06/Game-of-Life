from os import system
import time

def count_neighbours(grid, x_indx, y_indx, m, n):
    l = [-1, 0, 1]
    count = 0
    for i in l:
        for j in l:
            if x_indx+i >=0 and x_indx+i < n and y_indx+j >= 0 and y_indx+j < m:
                if i != 0 or j != 0:
                    count += grid[x_indx+i][y_indx+j]
    return count
n = int(input("rows:" ))
grid = []
m = int(input("col:" ))
for i in range(n):
    cell = []
    for a in range(m):
        cell.append(0)
    grid.append(cell)
clicks = int(input("clicks:" ))
for a in range(clicks):
    x = int(input("x-coordinate:" ))
    y = int(input("y-coordinate:" ))
    grid[x][y] = 1
# times = int(input("how many times function runs: "))
# for u in range(times):
while True:
    system("cls")
    grid_to_change = []
    for inner in grid:
        inner_copy = inner.copy()
        grid_to_change.append(inner_copy)
    for j in range(len(grid)):
        for k in range(len(grid)):
            x_indx = j
            y_indx = k
            final = count_neighbours(grid, x_indx, y_indx, m, n)
            # print("final: ", final)
                # count =  (grid[x_indx+1][y_indx] == 1)*1 + (grid[x_indx][y_indx+1] == 1)*1 + (grid[x_indx-1][y_indx] == 1)*1 + (grid[x_indx][y_indx - 1] == 1)*1 + (grid[x_indx+1][y_indx+1] == 1)*1 + (grid[x_indx-1][y_indx-1] == 1)*1 + (grid[x_indx+1][y_indx-1] == 1)*1 + (grid[x_indx-1][y_indx+1] == 1)*1
                # print("count:", count, "x_indx:", x_indx, "y_indx:", y_indx)
            if final < 2 or final > 3:
                grid_to_change[x_indx][y_indx] = 0
            elif final == 3:
                grid_to_change[x_indx][y_indx] = 1
    for u in grid_to_change:    
        print(u)
    print()
    grid = grid_to_change
    time.sleep(5)
