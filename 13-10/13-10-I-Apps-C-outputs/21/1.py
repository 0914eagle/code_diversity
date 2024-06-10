
def get_non_equivalence_relations(n):
    # Initialize a list to store the relations
    relations = []
    
    # Iterate over all possible pairs of elements in the set
    for i in range(n):
        for j in range(i+1, n):
            # Create a new relation and add it to the list
            relation = {(i, j)}
            relations.append(relation)
    
    # Return the number of relations modulo 10^9 + 7
    return len(relations) % (10**9 + 7)

def main():
    n = int(input())
    print(get_non_equivalence_relations(n))

if __name__ == '__main__':
    main()

