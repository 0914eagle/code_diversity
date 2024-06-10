
def input_sequence():
    n = int(input())
    sequence = list(map(int, input().split()))
    return n, sequence

def count_subsequences(sequence, k):
    # Initialize a dictionary to store the number of subsequences with length k
    subsequences = {}

    # Iterate over the sequence and count the number of subsequences with length k
    for i in range(len(sequence)):
        # If the current element is not in the dictionary, add it and set the count to 1
        if sequence[i] not in subsequences:
            subsequences[sequence[i]] = 1
        # If the current element is already in the dictionary, increment the count
        else:
            subsequences[sequence[i]] += 1

    # Return the number of subsequences with length k
    return len(subsequences)

def solve(n, sequence):
    # Initialize a list to store the number of subsequences with length k
    subsequences = [0] * (n + 1)

    # Iterate over the range of lengths and count the number of subsequences with each length
    for k in range(1, n + 1):
        subsequences[k] = count_subsequences(sequence, k)

    # Return the list of subsequences
    return subsequences

if __name__ == '__main__':
    n, sequence = input_sequence()
    result = solve(n, sequence)
    for i in range(n + 1):
        print(result[i])

