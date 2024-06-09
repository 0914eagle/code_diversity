
def f1(n, m):
    # Calculate the number of subsequences for each sequence
    # and return the sum modulo 10^9 + 7
    return sum(f2(n, m)) % 1000000007

def f2(n, m):
    # Initialize a list to store the number of subsequences for each sequence
    num_subsequences = [0] * (m + 1)
    num_subsequences[0] = 1

    # Iterate over each element in the sequence
    for i in range(1, n + 1):
        # Iterate over each possible value for the current element
        for j in range(1, m + 1):
            # If the current element is less than or equal to the maximum value,
            # add the number of subsequences for the previous element
            if j <= m:
                num_subsequences[j] += num_subsequences[j - 1]

    return num_subsequences

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(f1(n, m))

