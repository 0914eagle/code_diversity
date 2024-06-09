
def can_deploy_services(n, x1, x2, servers):
    # Sort the servers in non-decreasing order of their capacity
    servers.sort()
    # Initialize the number of servers used for each service as 0
    k1, k2 = 0, 0
    # Iterate through the servers from left to right
    for i, server in enumerate(servers, 1):
        # If the current server can provide at least x1 resource units and is not already used,
        # assign it to the first service and increment the number of servers used for the first service
        if server >= x1 and k1 == 0:
            k1 += 1
            servers[i-1] -= x1
        # If the current server can provide at least x2 resource units and is not already used,
        # assign it to the second service and increment the number of servers used for the second service
        elif server >= x2 and k2 == 0:
            k2 += 1
            servers[i-1] -= x2
        # If both services have already been assigned servers, break the loop
        if k1 > 0 and k2 > 0:
            break
    # If both services have been assigned servers, return True and the indices of the servers used
    if k1 > 0 and k2 > 0:
        return True, k1, k2, [i for i, server in enumerate(servers) if server < 0]
    # Otherwise, return False
    else:
        return False, 0, 0, []

n, x1, x2 = map(int, input().split())
servers = list(map(int, input().split()))
result = can_deploy_services(n, x1, x2, servers)
if result[0]:
    print("Yes")
    print(result[1], result[2])
    print(*result[3])
    print(*result[4])
else:
    print("No")

