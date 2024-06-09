
import math

def is_possible(A, N):
    # Calculate the perimeter of the cage
    perimeter = 4 * math.sqrt(N)
    # Calculate the area of the cage
    area = (perimeter / 2) ** 2
    # Check if the area is equal to A
    if area == A:
        return True
    else:
        return False

# Test the function with the sample input
A = 1.000000
N = 4.000000
print(is_possible(A, N)) # Should print "Diablo is happy!"

