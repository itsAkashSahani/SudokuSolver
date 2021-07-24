"""

This Is A Sudoku Solver.
You Just Have To Modify The Sudoku Grid Given
Below.

0 Represents Empty Fields

"""

grid = [
        [0, 0, 0, 0, 0, 0, 6, 8, 0],
        [0, 0, 0, 0, 7, 3, 0, 0, 9],
        [3, 0, 9, 0, 0, 0, 0, 0, 5],
        [4, 9, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 3, 0, 5, 0, 9, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 3, 6],
        [9, 6, 0, 0, 0, 0, 3, 0, 8],
        [7, 0, 0, 6, 8, 0, 0, 0, 0],
        [0, 2, 8, 0, 0, 0, 0, 0, 0],
       ]


#This function will check is move valid
def is_valid(grid, row, col, number):
  
  #Check the same num in row
  for x in range(9):
    if grid[row][x] == number:
      return False
  
  #Check the same num in column    
  for x in range(9):
    if grid[x][col] == number:
      return False


  corner_row = row - row % 3
  corner_col = col - col % 3
  
  #Check the same num in local field
  for x in range(3):
    for y in range(3):
      if grid[corner_row + x][corner_col + y] == number:
        return False
  return True


#Main Function
def solve(grid, row, col):
  if col == 9:
    if row == 8:
      return True
    
    row += 1
    col = 0
    
  if grid[row][col] > 0:
    return solve(grid, row, col + 1)
    
    
  for num in range(1, 10):
    if is_valid(grid, row, col, num):
      grid[row][col] = num
    
      if solve(grid, row, col + 1):
        return True
    
    grid[row][col] = 0
    
  return False


if solve(grid, 0, 0):
  print("Solution :")
  for i in range(9):
    for j in range(9):
      print(grid[i][j], end = " ")
    
    print()


else:
  print("There is no solution of this Sudoku !")




