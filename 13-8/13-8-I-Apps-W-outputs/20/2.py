
def get_longest_magical_permutation(s):
    # Find the longest magical permutation of length 2^x - 1
    for x in range(32, -1, -1):
        # Create a bitmask with the first x bits set to 1 and the rest set to 0
        bitmask = (1 << x) - 1
        # Iterate over all possible permutations of length 2^x - 1
        for i in range(1 << x):
            # Check if the permutation is magical
            if is_magical_permutation(i, bitmask, s):
                # If it is, return the length of the permutation and the permutation itself
                return x, get_permutation(i, bitmask)
    # If no magical permutation is found, return 0 and an empty list
    return 0, []

def is_magical_permutation(permutation, bitmask, s):
    # Check if the permutation is a valid magical permutation
    for i in range(len(permutation) - 1):
        # Calculate the bitwise xor of the current and next element in the permutation
        xor = permutation[i] ^ permutation[i + 1]
        # Check if the result is in the set S
        if xor not in s:
            return False
    return True

def get_permutation(permutation, bitmask):
    # Convert the integer permutation to a list of integers
    return [int(c) for c in bin(permutation)[2:]]

def main():
    s = set(map(int, input().split()))
    x, permutation = get_longest_magical_permutation(s)
    print(x)
    print(" ".join(map(str, permutation)))

if __name__ == "__main__":
    main()

