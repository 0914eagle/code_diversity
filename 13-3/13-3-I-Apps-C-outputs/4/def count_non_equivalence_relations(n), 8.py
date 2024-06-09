
def count_non_equivalence_relations(n):
    # Calculate the number of binary relations over a set of size n
    # that are symmetric, transitive, but not an equivalence relations
    count = 0
    
    # Iterate over all possible binary relations
    for i in range(2**n):
        # Convert the binary number to a list of bits
        bits = [int(b) for b in bin(i)[2:]]
        
        # Check if the relation is symmetric and transitive
        if all(bits[i] == bits[j] for i in range(n) for j in range(i+1, n)):
            # Check if the relation is not an equivalence relation
            if not all(bits[i] == 1 for i in range(n)):
                count += 1
    
    # Return the number of non-equivalence relations modulo 10^9 + 7
    return count % 1000000007

