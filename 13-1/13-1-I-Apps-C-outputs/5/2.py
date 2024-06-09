
def f1(n, t, a, b, d):
    # Calculate the fair share for each species
    fair_share = [t * d[i] / sum(d) for i in range(n)]
    
    # Initialize the allocation for each species
    allocation = [0] * n
    
    # Loop through each species and allocate the bandwidth
    for i in range(n):
        # Calculate the available bandwidth for the current species
        available_bandwidth = b[i] - a[i]
        
        # Calculate the maximum bandwidth that can be allocated for the current species
        max_allocation = min(available_bandwidth, fair_share[i])
        
        # Allocate the maximum bandwidth to the current species
        allocation[i] = max_allocation
        
        # Update the remaining bandwidth
        t -= max_allocation
    
    # Return the allocation for each species
    return allocation

def f2(n, t, a, b, d):
    # Calculate the fair share for each species
    fair_share = [t * d[i] / sum(d) for i in range(n)]
    
    # Initialize the allocation for each species
    allocation = [0] * n
    
    # Loop through each species and allocate the bandwidth
    for i in range(n):
        # Calculate the available bandwidth for the current species
        available_bandwidth = b[i] - a[i]
        
        # Calculate the maximum bandwidth that can be allocated for the current species
        max_allocation = min(available_bandwidth, fair_share[i])
        
        # Allocate the maximum bandwidth to the current species
        allocation[i] = max_allocation
        
        # Update the remaining bandwidth
        t -= max_allocation
    
    # Return the allocation for each species
    return allocation

if __name__ == '__main__':
    n = 3
    t = 10
    a = [0, 0, 0]
    b = [10, 10, 10]
    d = [1, 1, 1]
    print(f1(n, t, a, b, d))
    print(f2(n, t, a, b, d))

