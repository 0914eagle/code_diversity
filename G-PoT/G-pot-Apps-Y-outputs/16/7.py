
def find_minimum_pieces(a, b):
    lcm = a * b // math.gcd(a, b)
    return lcm

import math

input_values = input().split()
a = int(input_values[0])
b = int(input_values[1])

result = find_minimum_pieces(a, b)
print(result)
