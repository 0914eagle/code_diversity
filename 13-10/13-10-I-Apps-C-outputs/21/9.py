
def count_binary_relations(n):
    # Base case: if n is 1, there is only one relation, the empty set
    if n == 1:
        return 1
    
    # Initialize the number of relations to 0
    num_relations = 0
    
    # Iterate over all possible relations
    for i in range(2**n):
        # Convert the binary representation of i to a list of indices
        indices = [int(j) for j in bin(i)[2:]]
        
        # Check if the relation is symmetric and transitive
        if is_symmetric_and_transitive(indices, n):
            num_relations += 1
    
    # Return the number of relations modulo 10^9 + 7
    return num_relations % (10**9 + 7)

def is_symmetric_and_transitive(indices, n):
    # Check if the relation is symmetric
    for i in range(n):
        for j in range(i+1, n):
            if indices[i] != indices[j]:
                return False
    
    # Check if the relation is transitive
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if indices[i] == indices[j] and indices[j] == indices[k] and indices[i] != indices[k]:
                    return False
    
    # If the relation is symmetric and transitive, return True
    return True

if __name__ == '__main__':
    n = int(input())
    print(count_binary_relations(n))

