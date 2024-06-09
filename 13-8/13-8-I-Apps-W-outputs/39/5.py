
import itertools
import sys

def solve(n, m, k, b):
    # Initialize a list to store the distinct strings
    distinct_strings = []

    # Iterate over all possible combinations of characters from the set A
    for combination in itertools.combinations(range(k), n):
        # Initialize a string with the current combination of characters
        string = "".join(chr(ord('A') + c) for c in combination)

        # Append the string to the list of distinct strings
        distinct_strings.append(string)

    # Return the number of distinct strings modulo 998244353
    return len(distinct_strings) % 998244353

