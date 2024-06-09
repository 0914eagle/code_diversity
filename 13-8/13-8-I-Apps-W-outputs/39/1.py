
import sys

def count_distinct_strings(n, m, k, b):
    # Initialize a dictionary to store the count of each string
    string_counts = {}

    # Initialize a set to store the unique strings
    unique_strings = set()

    # Iterate over each move
    for i in range(m):
        # Get the current move
        current_move = b[i]

        # Iterate over each string
        for string in unique_strings:
            # Get the length of the string
            length = len(string)

            # Get the first k characters of the string
            first_k = string[:current_move]

            # Get the last k characters of the string
            last_k = string[-current_move:]

            # Get the reversed first k characters of the string
            rev_first_k = first_k[::-1]

            # Get the reversed last k characters of the string
            rev_last_k = last_k[::-1]

            # Add the four new strings to the dictionary
            string_counts[first_k + last_k] = string_counts.get(first_k + last_k, 0) + 1
            string_counts[last_k + first_k] = string_counts.get(last_k + first_k, 0) + 1
            string_counts[rev_first_k + last_k] = string_counts.get(rev_first_k + last_k, 0) + 1
            string_counts[rev_last_k + first_k] = string_counts.get(rev_last_k + first_k, 0) + 1

            # Add the four new strings to the set
            unique_strings.add(first_k + last_k)
            unique_strings.add(last_k + first_k)
            unique_strings.add(rev_first_k + last_k)
            unique_strings.add(rev_last_k + first_k)

    # Calculate the total number of distinct strings
    total_strings = sum(string_counts.values())

    # Return the total number of distinct strings modulo 998244353
    return total_strings % 998244353

n, m, k = map(int, input().split())
b = list(map(int, input().split()))
print(count_distinct_strings(n, m, k, b))

