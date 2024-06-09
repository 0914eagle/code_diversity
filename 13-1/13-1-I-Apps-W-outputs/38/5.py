
def f1(n, a):
    # Calculate the number of ways to flip some set of the roads
    # such that the resulting whole set of all roads is not confusing
    num_ways = 0
    
    # Iterate over all possible subsets of roads
    for subset in range(2**n):
        # Convert the binary representation of the subset to a list of road indices
        subset_list = [i for i in range(n) if subset & (1 << i)]
        
        # Check if the subset forms a directed cycle
        if is_confusing(n, a, subset_list):
            continue
        
        # If the subset does not form a directed cycle, increment the number of ways
        num_ways += 1
    
    return num_ways % (10**9 + 7)

def is_confusing(n, a, subset):
    # Check if the subset forms a directed cycle
    for i in range(n):
        if i in subset and a[i] in subset:
            return True
    return False

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(f1(n, a))

