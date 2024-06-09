
def add_comments(n, m, servers, commands):
    # Initialize an empty dictionary to map ip addresses to server names
    ip_to_name = {}
    
    # Iterate over the list of servers and populate the dictionary
    for server in servers:
        ip_to_name[server[1]] = server[0]
    
    # Initialize an empty list to store the modified commands
    modified_commands = []
    
    # Iterate over the list of commands and add the server name to the end of each line
    for command in commands:
        ip = command.split(" ")[1]
        name = ip_to_name[ip]
        modified_commands.append(command + " #" + name)
    
    return modified_commands

