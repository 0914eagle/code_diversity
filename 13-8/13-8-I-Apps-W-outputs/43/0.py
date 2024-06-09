
def solve(n, m, servers, commands):
    server_dict = {}
    for name, ip in servers:
        server_dict[ip] = name
    
    result = []
    for command, ip in commands:
        result.append(f"{command} {ip}; # {server_dict[ip]}")
    
    return result

