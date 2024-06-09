
def count_binary_relations(n):
    # Calculate the number of binary relations
    num_relations = (n * (n - 1)) // 2
    
    # Calculate the number of equivalence relations
    num_equivalence_relations = 1
    for i in range(2, n + 1):
        num_equivalence_relations *= i
    
    # Calculate the number of non-equivalence relations
    num_non_equivalence_relations = num_relations - num_equivalence_relations
    
    # Return the number of non-equivalence relations modulo 10^9 + 7
    return num_non_equivalence_relations % 1000000007

