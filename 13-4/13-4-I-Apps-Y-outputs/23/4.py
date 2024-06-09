
import math

n, a = map(int, input().split())

total_squares = n ** 2
white_squares = a
black_squares = total_squares - white_squares

print(black_squares)

