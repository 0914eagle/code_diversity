
def solve(n, m, servers, commands):
    # Create a dictionary to map IP addresses to server names
    ip_to_name = {server[1]: server[0] for server in servers}
    
    # Iterate through the commands and add the server name to the end of each line
    for i in range(len(commands)):
        command = commands[i]
        ip = command.split()[1]
        name = ip_to_name[ip]
        commands[i] += " #" + name
    
    return commands

