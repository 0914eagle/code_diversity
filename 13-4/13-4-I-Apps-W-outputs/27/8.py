
def f1(n, m):
    # Calculate the number of subsequences for each sequence of length n
    # and return the sum modulo 10^9 + 7
    return sum(f2(n, m)) % (10**9 + 7)

def f2(n, m):
    # Initialize a list to store the number of subsequences for each sequence of length n
    num_subsequences = [0] * (n + 1)
    num_subsequences[0] = 1

    # Iterate over the elements of the sequence
    for i in range(1, n + 1):
        # Initialize a set to store the unique elements in the subsequence
        unique_elements = set()

        # Iterate over the previous subsequence
        for j in range(i):
            # If the current element is not in the unique elements set, add it to the set and increment the number of subsequences
            if num_subsequences[j] > 0 and num_subsequences[j] not in unique_elements:
                unique_elements.add(num_subsequences[j])
                num_subsequences[i] += 1

        # If the current element is not in the unique elements set, add it to the set and increment the number of subsequences
        if i not in unique_elements:
            unique_elements.add(i)
            num_subsequences[i] += 1

    return num_subsequences

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(f1(n, m))

