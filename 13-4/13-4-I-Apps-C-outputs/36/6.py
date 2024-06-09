
def get_jokes(n, v, supervisors):
    # Initialize a set to store the jokes
    jokes = set()
    
    # Add the jokes told by the CEO (person with label 1)
    jokes.add(v[0])
    
    # Iterate through the supervisors
    for supervisor, subordinate in supervisors:
        # If the subordinate tells a joke that is not told by the CEO or by their supervisor, add it to the set
        if v[subordinate] not in jokes and v[supervisor] not in jokes:
            jokes.add(v[subordinate])
    
    return len(jokes)

def get_consecutive_sets(n, v, supervisors):
    # Initialize a set to store the consecutive sets of jokes
    consecutive_sets = set()
    
    # Iterate through the jokes
    for i in range(1, n + 1):
        # If the joke is told by the CEO or by their supervisor, skip it
        if i in v or i in supervisors:
            continue
        
        # Initialize a set to store the jokes in the current consecutive set
        current_set = set()
        
        # Add the current joke to the set
        current_set.add(i)
        
        # Iterate through the supervisors
        for supervisor, subordinate in supervisors:
            # If the subordinate tells a joke that is in the current set, add it to the set
            if subordinate in current_set:
                current_set.add(v[supervisor])
        
        # If the current set is not empty, add it to the set of consecutive sets
        if current_set:
            consecutive_sets.add(frozenset(current_set))
    
    return len(consecutive_sets)

def main():
    n = int(input())
    v = list(map(int, input().split()))
    supervisors = []
    for _ in range(n - 1):
        supervisors.append(tuple(map(int, input().split())))
    
    print(get_jokes(n, v, supervisors))
    print(get_consecutive_sets(n, v, supervisors))

if __name__ == '__main__':
    main()

