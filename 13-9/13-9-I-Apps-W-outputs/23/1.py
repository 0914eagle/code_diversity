
def can_deploy_services(n, x1, x2, c):
    # Sort the servers in descending order of their specifications
    c_sorted = sorted(c, reverse=True)
    
    # Initialize the number of servers used for each service
    k1 = 0
    k2 = 0
    
    # Loop through the servers and allocate them to either service 1 or service 2
    for i in range(n):
        if x1 // c_sorted[i] > 0:
            k1 += 1
            x1 -= c_sorted[i]
        elif x2 // c_sorted[i] > 0:
            k2 += 1
            x2 -= c_sorted[i]
        else:
            break
    
    # Check if both services can be deployed with the allocated servers
    if k1 > 0 and k2 > 0:
        return "Yes"
    else:
        return "No"

