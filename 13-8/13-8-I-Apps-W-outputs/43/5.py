
def solve(n, m):
    # Split the input into the server names and IP addresses
    server_names = input().split()
    server_ips = input().split()

    # Create a dictionary to map IP addresses to server names
    ip_to_name = {ip: name for name, ip in zip(server_names, server_ips)}

    # Iterate through the commands and add the server name to the end of each line
    for i in range(m):
        command, ip = input().split()
        name = ip_to_name[ip]
        print(f"{command} {ip}; # {name}")

    return ""

