
def get_permutation(b):
    # Initialize the permutation as the identity permutation
    permutation = list(range(1, len(b) + 1))
    # Loop through each element in the permutation
    for i in range(len(b)):
        # If the element is not in its correct position, find the correct position and swap it
        if permutation[i] != i + 1:
            correct_position = permutation.index(i + 1)
            permutation[i], permutation[correct_position] = permutation[correct_position], permutation[i]
    return permutation

def is_strictly_increasing(a):
    return all(a[i] < a[i + 1] for i in range(len(a) - 1))

def solve(b):
    # Get the permutation of the encrypted sequence
    permutation = get_permutation(b)
    # Check if the permutation leads to a strictly increasing sequence
    a = [b[0]]
    for i in range(1, len(b)):
        a.append(a[i - 1] ^ b[permutation[i]])
    if is_strictly_increasing(a):
        return "Yes\n" + " ".join(str(b[i - 1]) for i in permutation)
    else:
        return "No"

if __name__ == '__main__':
    n = int(input())
    b = list(map(int, input().split()))
    print(solve(b))

