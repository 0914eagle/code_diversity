
def f1(n, roads):
    # Calculate the number of ways to flip some set of the roads
    # such that the resulting whole set of all roads is not confusing
    num_ways = 0
    
    # Iterate over all possible subsets of the roads
    for subset in range(1, 2**n):
        # Check if the subset forms a directed cycle
        if is_confusing(subset, roads):
            continue
        # Increment the number of ways if the subset is not confusing
        num_ways += 1
    
    return num_ways % 1000000007

def f2(n, roads):
    # Calculate the number of ways to flip some set of the roads
    # such that the resulting whole set of all roads is not confusing
    num_ways = 0
    
    # Iterate over all possible subsets of the roads
    for subset in range(1, 2**n):
        # Check if the subset forms a directed cycle
        if is_confusing(subset, roads):
            continue
        # Increment the number of ways if the subset is not confusing
        num_ways += 1
    
    return num_ways % 1000000007

def is_confusing(subset, roads):
    # Check if the subset forms a directed cycle
    for i in range(n):
        if (subset >> i) & 1:
            if roads[i] == i:
                return True
    
    return False

if __name__ == '__main__':
    n = int(input())
    roads = list(map(int, input().split()))
    print(f1(n, roads))
    print(f2(n, roads))

