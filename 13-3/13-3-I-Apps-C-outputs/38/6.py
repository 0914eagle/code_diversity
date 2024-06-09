
def count_relations(n):
    # Base case: if n is 1, there is only one relation (the empty relation)
    if n == 1:
        return 1

    # Initialize the number of relations to 0
    num_relations = 0

    # Iterate over all possible relations
    for i in range(2**n):
        # Convert the binary representation of i to a list of bits
        bits = [int(bit) for bit in bin(i)[2:]]

        # Check if the relation is symmetric and transitive
        if is_symmetric_and_transitive(bits, n):
            num_relations += 1

    # Return the number of relations modulo 10^9 + 7
    return num_relations % (10**9 + 7)

def is_symmetric_and_transitive(bits, n):
    # Check if the relation is symmetric
    for i in range(n):
        for j in range(i+1, n):
            if bits[i] != bits[j] and bits[j] == 1:
                return False

    # Check if the relation is transitive
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if bits[i] == 1 and bits[j] == 1 and bits[k] == 1 and i != j != k:
                    return False

    # If the relation is symmetric and transitive, return True
    return True

print(count_relations(int(input())))

