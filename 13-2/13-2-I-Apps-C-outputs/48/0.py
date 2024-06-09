
import math

def solve(A, B):
    # Calculate the sum of distances between each pair of numbers in the interval [A, B]
    sum_distances = 0
    for i in range(A, B+1):
        for j in range(A, B+1):
            sum_distances += distance(i, j)
    
    # Return the result modulo 1000000007
    return sum_distances % 1000000007

def distance(a, b):
    # Convert the numbers to strings
    a_str = str(a)
    b_str = str(b)
    
    # Pad the shorter string with leading zeroes
    if len(a_str) < len(b_str):
        a_str = '0' * (len(b_str) - len(a_str)) + a_str
    elif len(b_str) < len(a_str):
        b_str = '0' * (len(a_str) - len(b_str)) + b_str
    
    # Calculate the distance between the two numbers
    distance = 0
    for i in range(len(a_str)):
        distance += abs(int(a_str[i]) - int(b_str[i]))
    
    return distance

