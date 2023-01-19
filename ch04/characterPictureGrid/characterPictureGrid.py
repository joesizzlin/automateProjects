# Character Picture Grid Project

# starting grid assigned to lists
grid = [['.', '.', '.', '.', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.'],
         ['O', 'O', 'O', 'O', '.', '.'],
         ['O', 'O', 'O', 'O', 'O', '.'],
         ['.', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', '.'],
         ['O', 'O', 'O', 'O', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.']]

def output(grid):                                       # define the output function
    for y in range(len(grid[0])):                       # iterates over the columns of the grid
        print()
        for x in range(len(grid)):                      # iterates over the rows of the grid 
            print(grid[x][y], end=' ')                  # prints the character at the current row and column. end=' ' creates a space
    print()                                             # after the loop finishes, prints a newline character to move to next line 
                                                        # The outer loop then moves to the next column and the process repeats.
output(grid)                                            #calls the above function and passes 'grid' variable as an argument