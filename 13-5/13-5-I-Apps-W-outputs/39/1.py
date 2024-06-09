
def f1(n, roads):
    # Calculate the number of ways to flip some set of the roads
    # such that the resulting whole set of all roads is not confusing
    num_ways = 0
    
    # Iterate over all possible subsets of the roads
    for subset in range(2**n):
        # Convert the binary representation of the subset to a list of indices
        subset_indices = [i for i in range(n) if subset & (1 << i)]
        
        # Check if the subset forms a directed cycle
        if is_confusing(subset_indices, roads):
            continue
        
        # Increment the number of ways if the subset is not confusing
        num_ways += 1
    
    return num_ways % 1000000007

def f2(...):
    # Your code here
    pass

if __name__ == '__main__':
    n = int(input())
    roads = list(map(int, input().split()))
    print(f1(n, roads))

