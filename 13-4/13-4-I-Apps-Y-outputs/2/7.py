
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
A = 1.0
N = 4.0
print(is_possible(A, N)) # Should print "Diablo is happy!"

# Test the function with a larger input
A = 100.0
N = 1000.0
print(is_possible(A, N)) # Should print "Need more materials!"

