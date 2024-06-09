
N = int(input())
A = int(input())

# Calculate the total number of squares
total_squares = N ** 2

# Calculate the number of squares that will be painted white
white_squares = A

# Calculate the number of squares that will be painted black
black_squares = total_squares - white_squares

print(black_squares)

