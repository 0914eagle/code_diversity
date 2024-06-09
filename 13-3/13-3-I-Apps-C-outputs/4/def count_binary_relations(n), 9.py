
def count_binary_relations(n):
    # Calculate the number of binary relations
    num_relations = (n * (n - 1)) // 2
    
    # Subtract the number of equivalence relations
    num_equivalence_relations = n
    for i in range(1, n):
        num_equivalence_relations += i
    num_relations -= num_equivalence_relations
    
    # Return the result modulo 10^9 + 7
    return num_relations % 1000000007

