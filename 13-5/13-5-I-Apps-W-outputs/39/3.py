
import itertools

def f1(n, a):
    # Calculate the number of ways to flip some set of the roads
    # such that the resulting whole set of all roads is not confusing
    num_ways = 0
    
    # Iterate over all possible subsets of roads
    for subset in itertools.combinations(range(n), n):
        # Check if the subset forms a directed cycle
        if is_confusing(subset, a):
            continue
        num_ways += 1
    
    return num_ways % (10**9 + 7)

def is_confusing(subset, a):
    # Check if the subset forms a directed cycle
    for i in range(len(subset)):
        if a[subset[i]] in subset[i+1:]:
            return True
    return False

def f2(...):
    # Your code for the second function goes here
    pass

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(f1(n, a))

