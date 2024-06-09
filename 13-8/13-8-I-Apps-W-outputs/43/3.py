
def solve(n, m):
    servers = {}
    for _ in range(n):
        name, ip = input().split()
        servers[ip] = name
    
    for _ in range(m):
        command, ip = input().split()
        print(f"{command} {ip}; # {servers[ip]}")

