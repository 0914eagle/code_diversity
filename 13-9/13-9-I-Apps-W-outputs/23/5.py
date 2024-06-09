
def solve(n, x1, x2, c):
    # Check if the total resource units provided by all servers is greater than or equal to the sum of resource units required by both services
    if sum(c) < x1 + x2:
        return "No"
    
    # Initialize variables
    k1 = 0
    k2 = 0
    servers1 = []
    servers2 = []
    
    # Loop through each server and check if it can be used for deploying both services
    for i in range(n):
        # Check if the server can be used for deploying service 1
        if c[i] >= x1:
            k1 += 1
            servers1.append(i + 1)
        
        # Check if the server can be used for deploying service 2
        if c[i] >= x2:
            k2 += 1
            servers2.append(i + 1)
    
    # Check if both services can be deployed using the available servers
    if k1 == 0 or k2 == 0:
        return "No"
    
    return "Yes\n" + str(k1) + " " + str(k2) + "\n" + " ".join(map(str, servers1)) + "\n" + " ".join(map(str, servers2))

