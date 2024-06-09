
import math

def is_possible(A, N):
    # Calculate the perimeter of the cage
    perimeter = 4 * N
    # Calculate the area of the cage
    area = (perimeter / 2) ** 2
    # Check if the area is equal to A
    if area == A:
        return True
    else:
        return False

A, N = map(float, input().split())
if is_possible(A, N):
    print("Diablo is happy!")
else:
    print("Need more materials!")

