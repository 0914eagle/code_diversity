
def can_deploy_services(n, x1, x2, c):
    # Sort the servers in descending order of their specifications
    c_sorted = sorted(c, reverse=True)
    
    # Initialize the number of servers used for each service
    k1 = 0
    k2 = 0
    
    # Loop through the servers and assign them to either service 1 or service 2
    for i, ci in enumerate(c_sorted, 1):
        if x1 / ci <= n - i + 1 and x2 / ci <= n - i + 1:
            if i % 2 == 1:
                k1 += 1
            else:
                k2 += 1
        else:
            break
    
    # If both services can be deployed, return the number of servers used for each service and the indices of the servers used
    if k1 > 0 and k2 > 0:
        return "Yes", k1, k1, k2
    else:
        return "No", 0, 0, 0

