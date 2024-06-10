
def count_binary_relations(n):
    # Initialize the number of relations to 0
    num_relations = 0
    
    # Iterate over all possible relations
    for i in range(2**n):
        # Convert the binary representation of i to a list of bits
        bits = [int(b) for b in bin(i)[2:]]
        
        # Check if the relation is symmetric and transitive
        if is_symmetric_and_transitive(bits, n):
            # Increment the number of relations
            num_relations += 1
    
    # Return the number of relations modulo 10^9 + 7
    return num_relations % (10**9 + 7)

def is_symmetric_and_transitive(bits, n):
    # Check if the relation is symmetric
    if not is_symmetric(bits, n):
        return False
    
    # Check if the relation is transitive
    if not is_transitive(bits, n):
        return False
    
    # If both checks pass, return True
    return True

def is_symmetric(bits, n):
    # Iterate over all possible pairs of elements in the set
    for i in range(n):
        for j in range(i+1, n):
            # Check if the relation is symmetric
            if bits[i] != bits[j]:
                return False
    
    # If all pairs are symmetric, return True
    return True

def is_transitive(bits, n):
    # Iterate over all possible triples of elements in the set
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                # Check if the relation is transitive
                if bits[i] != bits[j] and bits[j] != bits[k] and bits[i] != bits[k]:
                    return False
    
    # If all triples are transitive, return True
    return True

if __name__ == '__main__':
    n = int(input())
    print(count_binary_relations(n))

