
def f1(n, t, a, b, d):
    # Calculate the fair share for each species
    fair_share = [t * d[i] / sum(d) for i in range(n)]
    
    # Initialize the allocation for each species
    allocation = [0] * n
    
    # Loop through each species and allocate the bandwidth
    for i in range(n):
        # Calculate the available bandwidth for the current species
        available_bandwidth = b[i] - a[i]
        
        # Calculate the difference between the fair share and the available bandwidth
        difference = fair_share[i] - available_bandwidth
        
        # If the difference is positive, allocate the available bandwidth
        if difference > 0:
            allocation[i] = available_bandwidth
        # If the difference is negative, allocate the fair share
        else:
            allocation[i] = fair_share[i]
    
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
        
        # Calculate the difference between the fair share and the available bandwidth
        difference = fair_share[i] - available_bandwidth
        
        # If the difference is positive, allocate the available bandwidth
        if difference > 0:
            allocation[i] = available_bandwidth
        # If the difference is negative, allocate the fair share
        else:
            allocation[i] = fair_share[i]
    
    # Return the allocation for each species
    return allocation

if __name__ == '__main__':
    n = 3
    t = 10
    a = [0, 0, 0]
    b = [10, 10, 10]
    d = [1, 1, 1]
    allocation = f1(n, t, a, b, d)
    print(allocation)
    allocation = f2(n, t, a, b, d)
    print(allocation)

