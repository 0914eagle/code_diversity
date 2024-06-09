
def can_deploy_services(n, x1, x2, c):
    # Sort the servers by the amount of resource units they provide
    sorted_servers = sorted(c, reverse=True)

    # Initialize the variables to keep track of the servers used for each service
    k1, k2 = 0, 0
    servers1, servers2 = [], []

    # Loop through the servers and assign them to either service 1 or service 2
    for i, server in enumerate(sorted_servers, 1):
        if x1 // i <= server:
            k1 += 1
            servers1.append(i)
        elif x2 // i <= server:
            k2 += 1
            servers2.append(i)

    # If both services can be deployed, return the answers
    if k1 > 0 and k2 > 0:
        return "Yes", k1, k2, servers1, servers2

    # Otherwise, return that it is not possible to deploy both services
    return "No", 0, 0, [], []

