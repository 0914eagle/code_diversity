
def solve(n, m, servers, commands):
    # Initialize an empty dictionary to map IP addresses to server names
    ip_to_name = {}

    # Iterate over the list of servers and populate the dictionary
    for server in servers:
        ip_to_name[server[1]] = server[0]

    # Iterate over the list of commands and add the server names to the end of each line
    for i in range(len(commands)):
        command = commands[i]
        ip = command.split(" ")[1]
        name = ip_to_name[ip]
        commands[i] = command + " #" + name

    return commands

