
def solve(n, m, servers, commands):
    # Initialize an empty dictionary to map IP addresses to server names
    ip_to_name = {}
    
    # Iterate over the list of servers and populate the dictionary
    for server in servers:
        ip_to_name[server[1]] = server[0]
    
    # Iterate over the list of commands and append the server name to each command
    for i in range(len(commands)):
        ip = commands[i].split(" ")[1]
        commands[i] += " #" + ip_to_name[ip]
    
    return commands

