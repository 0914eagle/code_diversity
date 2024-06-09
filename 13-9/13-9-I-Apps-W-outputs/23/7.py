
def can_deploy_services(n, x1, x2, servers):
    # Sort the servers in non-decreasing order of their specifications
    sorted_servers = sorted(servers)

    # Initialize the number of servers used for each service to 0
    k1, k2 = 0, 0

    # Iterate through the servers in non-decreasing order of their specifications
    for i, c in enumerate(sorted_servers, start=1):
        # Calculate the number of servers needed to process the first service
        needed1 = (x1 - k1 * c) // (k1 + 1)

        # Calculate the number of servers needed to process the second service
        needed2 = (x2 - k2 * c) // (k2 + 1)

        # If it is possible to deploy both services using the current server, update the number of servers used for each service
        if needed1 <= 0 and needed2 <= 0:
            k1 += 1
            k2 += 1
        # If it is only possible to deploy one service using the current server, update the number of servers used for that service
        elif needed1 <= 0:
            k2 += 1
        elif needed2 <= 0:
            k1 += 1

        # If it is not possible to deploy either service using the current server, return False
        if needed1 > 0 and needed2 > 0:
            return False

    # If it is possible to deploy both services using the given servers, return True and the indices of the servers used for each service
    return True, [i for i in range(1, n + 1) if servers[i - 1] >= needed1], [i for i in range(1, n + 1) if servers[i - 1] >= needed2]


n, x1, x2 = map(int, input().split())
servers = list(map(int, input().split()))

result = can_deploy_services(n, x1, x2, servers)
if result[0]:
    print("Yes")
    print(result[1][0], result[2][0])
    print(*result[1][1:], sep=" ")
    print(*result[2][1:], sep=" ")
else:
    print("No")

