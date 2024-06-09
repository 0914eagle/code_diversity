
def f1(n, a):
    # Calculate the number of ways to flip some set of the roads
    # such that the resulting whole set of all roads is not confusing
    mod = 1000000007
    num_ways = 0
    
    # Iterate over all possible sets of roads
    for i in range(1, 2**n):
        # Convert the binary representation of i to a list of booleans
        # indicating which roads to flip
        flip_roads = [bool(i & (1 << j)) for j in range(n)]
        
        # Check if the resulting network is not confusing
        if not is_confusing(n, a, flip_roads):
            num_ways += 1
    
    return num_ways % mod

def f2(n, a):
    # Calculate the number of ways to flip some set of the roads
    # such that the resulting whole set of all roads is not confusing
    mod = 1000000007
    num_ways = 0
    
    # Iterate over all possible sets of roads
    for i in range(1, 2**n):
        # Convert the binary representation of i to a list of booleans
        # indicating which roads to flip
        flip_roads = [bool(i & (1 << j)) for j in range(n)]
        
        # Check if the resulting network is not confusing
        if not is_confusing(n, a, flip_roads):
            num_ways += 1
    
    return num_ways % mod

def is_confusing(n, a, flip_roads):
    # Check if the resulting network is not confusing
    for i in range(n):
        if flip_roads[i]:
            a[i], a[a[i] - 1] = a[a[i] - 1], a[i]
    
    # Check if there is a sequence of distinct towns A_1, A_2, ..., A_{k}
    # such that for every 1 ≤ i < k there is a road from town A_{i} to town A_{i} + 1
    # and another road from town A_{k} to town A_1
    for i in range(n):
        visited = [False] * n
        queue = [i]
        visited[i] = True
        while queue:
            curr = queue.pop(0)
            for j in range(n):
                if a[curr] == j + 1 and not visited[j]:
                    visited[j] = True
                    queue.append(j)
            if visited[i]:
                return True
    
    return False

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(f1(n, a))
    print(f2(n, a))

