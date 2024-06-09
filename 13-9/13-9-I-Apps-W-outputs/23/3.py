
def solve(n, x1, x2, c):
    # Check if the total resource units provided by all servers is greater than or equal to the total resource units required by both services
    if sum(c) < x1 + x2:
        return "No"
    
    # Initialize the number of servers used for each service
    k1 = 0
    k2 = 0
    
    # Initialize the indices of the servers used for each service
    servers1 = []
    servers2 = []
    
    # Loop through the servers
    for i in range(n):
        # Check if the current server provides enough resource units for both services
        if c[i] >= x1 and c[i] >= x2:
            # Add the current server to the list of servers used for the first service
            servers1.append(i + 1)
            k1 += 1
            # Subtract the resource units provided by the current server from the total resource units required by the first service
            x1 -= c[i]
            # Check if the first service has been deployed using all the required resource units
            if x1 == 0:
                break
        elif c[i] >= x2:
            # Add the current server to the list of servers used for the second service
            servers2.append(i + 1)
            k2 += 1
            # Subtract the resource units provided by the current server from the total resource units required by the second service
            x2 -= c[i]
            # Check if the second service has been deployed using all the required resource units
            if x2 == 0:
                break
    
    # Check if both services have been deployed using all the required resource units
    if x1 == 0 and x2 == 0:
        return "Yes\n" + str(k1) + "\n" + " ".join(map(str, servers1)) + "\n" + str(k2) + "\n" + " ".join(map(str, servers2))
    else:
        return "No"

