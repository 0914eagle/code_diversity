
def solve(n, m, names, ips, commands):
    # Initialize an empty dictionary to map ips to names
    ip_to_name = {}

    # Iterate over the list of names and ips
    for name, ip in zip(names, ips):
        # Add the ip and name to the dictionary
        ip_to_name[ip] = name

    # Initialize an empty list to store the modified commands
    modified_commands = []

    # Iterate over the list of commands
    for command in commands:
        # Split the command into the ip and command parts
        ip, command = command.split(" ")

        # Check if the ip is in the dictionary
        if ip in ip_to_name:
            # Get the name associated with the ip
            name = ip_to_name[ip]

            # Add the name to the command and append it to the list of modified commands
            modified_commands.append(f"{command} {ip}; # {name}")

    # Return the list of modified commands
    return modified_commands

