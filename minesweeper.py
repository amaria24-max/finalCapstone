
def minesweeper(grid):

   # Define grid ranges (5x5 grid)
   # Create for loops to iterate over rows and columns 
   # Check for "-" that appear on the grid
   # Set up count for adjacent neighbours
   for row in range(5):
      for col in range(5):
         if grid[row][col] == "-":
            count = 0

            # Create nester loops to iterate over surrounding neighbours
            # Set ranges to stay within the board
            # Add to the count if neighbour is '#' 
            for row_mine in range(max(0, row-1), min(5, row+2)):
               for col_mine in range(max(0, col-1), min(5, col+2)):
                  if grid[row_mine][col_mine] == "#":
                     count += 1
            grid[row][col] = str(count)

   return grid



grid = [["-", "-", "-", "#", "#"],
        ["-", "#", "#", "-", "-"],
        ["#", "#", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["#", "-", "#", "-", "-"]]

print("\nThis is the minesweeper grid\n")

# Print the minesweeper grid
for row in grid:
   for num in row:
      print(num, end= " ")
   print()

print("\nBelow is the number of mines adjacent to empty spaces.\n")

# Print the grid with number of mines adjacent to empty spaces
for row in minesweeper(grid):
   for num in row:
      print(num, end = " ")
   print()

print("\nThis is the index value for each row:\n")

# Use enumerate to keep count of index values for each row
for index, count in enumerate(grid, start=0):
   print(f'Row: {index}' )
   for index, count in enumerate(count, start=0):
      print(f'Index {index} contains the value {count}')
   print()
