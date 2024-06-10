
def count_binary_relations(n):
    # Base case: if n is 1, there is only one relation, the empty relation
    if n == 1:
        return 1
    
    # Initialize a list to store the relations
    relations = []
    
    # Iterate over all possible pairs of elements in the set
    for i in range(n):
        for j in range(i, n):
            # If i is not equal to j, create a new relation with the pair (i, j)
            if i != j:
                relations.append((i, j))
    
    # Iterate over the relations and check if they are symmetric and transitive
    symmetric_transitive_relations = 0
    for relation in relations:
        # Check if the relation is symmetric
        if (relation[1], relation[0]) in relations:
            # Check if the relation is transitive
            if (relation[0], relation[1]) in relations and (relation[1], relation[2]) in relations:
                symmetric_transitive_relations += 1
    
    # Return the number of symmetric and transitive relations modulo 10^9 + 7
    return symmetric_transitive_relations % 1000000007

def main():
    n = int(input())
    print(count_binary_relations(n))

if __name__ == '__main__':
    main()

