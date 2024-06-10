
def find_minimal_signed_binary_representation(n):
    # Initialize the signed binary representation with all zeros
    sb_repr = [0] * (n.bit_length() - 1)

    # Iterate through the bits of the binary representation of n, starting from the most significant bit
    for i in range(n.bit_length() - 1, -1, -1):
        # If the current bit is set to 1, set the corresponding position in the signed binary representation to +1
        if n & (1 << i):
            sb_repr[i] = 1
        # If the current bit is set to 0, set the corresponding position in the signed binary representation to -1
        else:
            sb_repr[i] = -1

    # Return the signed binary representation
    return sb_repr

def get_minimal_signed_binary_representation(n):
    # Initialize the minimal signed binary representation with all zeros
    minimal_sb_repr = [0] * (n.bit_length() - 1)

    # Iterate through the possible signed binary representations of n
    for sb_repr in itertools.product((-1, 0, 1), repeat=n.bit_length() - 1):
        # If the current signed binary representation has fewer non-zero digits than the current minimal signed binary representation, update the minimal signed binary representation
        if sum(sb_repr) < sum(minimal_sb_repr):
            minimal_sb_repr = sb_repr

    # Return the minimal signed binary representation
    return minimal_sb_repr

def main():
    # Read a positive integer n from standard input
    n = int(input())

    # Find the minimal signed binary representation of n
    minimal_sb_repr = get_minimal_signed_binary_representation(n)

    # Print the minimal signed binary representation of n
    print("".join(str(x) for x in minimal_sb_repr))

if __name__ == '__main__':
    main()

