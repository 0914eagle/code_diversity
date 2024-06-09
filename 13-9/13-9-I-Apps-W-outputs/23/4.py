
def solve(n, x1, x2, c):
    # Check if the total resource units provided by all servers is enough to deploy both services
    total_c = sum(c)
    if total_c < x1 + x2:
        return "No"
    
    # Initialize the number of servers used for each service
    k1 = 0
    k2 = 0
    
    # Initialize the list of servers used for each service
    servers1 = []
    servers2 = []
    
    # Iterate through the servers and assign them to the appropriate service
    for i in range(n):
        # Check if the current server provides enough resource units to deploy the first service
        if c[i] >= x1:
            k1 += 1
            servers1.append(i + 1)
        # Check if the current server provides enough resource units to deploy the second service
        if c[i] >= x2:
            k2 += 1
            servers2.append(i + 1)
    
    # Check if at least one server is used for each service
    if k1 == 0 or k2 == 0:
        return "No"
    
    return "Yes", k1, k2, servers1, servers2

