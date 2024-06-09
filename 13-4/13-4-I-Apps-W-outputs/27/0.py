
def f1(n, m):
    # Calculate the number of subsequences for each sequence
    # and return the sum modulo 10^9 + 7
    return sum(f2(n, m)) % (10**9 + 7)

def f2(n, m):
    # Initialize a list to store the number of subsequences for each sequence
    num_subsequences = [0] * (n + 1)
    num_subsequences[0] = 1

    # Iterate over the elements of the sequence
    for i in range(1, n + 1):
        # Initialize a variable to store the number of subsequences for the current element
        curr_num_subsequences = 0

        # Iterate over the previous elements of the sequence
        for j in range(i):
            # If the current element is greater than or equal to the previous element,
            # add the number of subsequences for the previous element to the current element
            if m - i + j >= 0:
                curr_num_subsequences += num_subsequences[j]

        # Add the number of subsequences for the current element to the list
        num_subsequences[i] = curr_num_subsequences

    return num_subsequences

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(f1(n, m))

