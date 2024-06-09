
def solve(n, x1, x2, c):
    # Initialize variables
    servers_used = [0] * n
    servers_needed = [0] * n
    total_resource_units = sum(c)
    service_1_resource_units = x1
    service_2_resource_units = x2
    
    # Check if the total resource units are sufficient
    if total_resource_units < service_1_resource_units + service_2_resource_units:
        return "No"
    
    # Sort the servers by their resource units in descending order
    sorted_servers = sorted(range(n), key=lambda i: c[i], reverse=True)
    
    # Assign servers to service 1
    for i in sorted_servers:
        if service_1_resource_units > 0:
            servers_used[i] = 1
            service_1_resource_units -= c[i]
    
    # Assign servers to service 2
    for i in sorted_servers:
        if service_2_resource_units > 0 and servers_used[i] == 0:
            servers_used[i] = 2
            service_2_resource_units -= c[i]
    
    # Check if both services can be deployed
    if service_1_resource_units > 0 or service_2_resource_units > 0:
        return "No"
    
    # Count the number of servers used for each service
    for i in range(n):
        if servers_used[i] == 1:
            servers_needed[0] += 1
        elif servers_used[i] == 2:
            servers_needed[1] += 1
    
    # Print the output
    return "Yes\n{0} {1}\n{2}\n{3}".format(servers_needed[0], servers_needed[1], " ".join(str(i + 1) for i in range(n) if servers_used[i] == 1), " ".join(str(i + 1) for i in range(n) if servers_used[i] == 2))

