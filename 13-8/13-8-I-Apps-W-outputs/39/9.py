
import itertools
import math

def solve(n, m, a, b):
    # Calculate the number of distinct strings
    num_strings = math.factorial(n)
    
    # Iterate over all possible moves
    for i in range(m):
        # Calculate the number of strings that can be obtained by applying the move
        num_strings_after_move = 0
        for string in itertools.product(a, repeat=n):
            # Check if the string can be obtained by applying the move
            if can_apply_move(string, b[i]):
                num_strings_after_move += 1
        
        # Update the number of distinct strings
        num_strings = (num_strings * num_strings_after_move) % 998244353
    
    return num_strings

def can_apply_move(string, k):
    # Check if the string can be obtained by applying the move
    return (string[:k] == string[:k][::-1] and string[k:] == string[k:][::-1]) or (string[:k] == string[n-k:][::-1] and string[k:] == string[:n-k])

