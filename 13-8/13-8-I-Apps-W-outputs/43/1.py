
def solve(commands, servers):
    server_names = {server["ip"]: server["name"] for server in servers}
    return [f'{command} {ip}; # {server_names[ip]}' for command, ip in commands]

