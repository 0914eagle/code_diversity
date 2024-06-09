
def get_server_name(ip, servers):
    for server in servers:
        if server[1] == ip:
            return server[0]
    return None

def add_comments(commands, servers):
    result = []
    for command in commands:
        ip = command.split(" ")[1]
        name = get_server_name(ip, servers)
        result.append(f"{command} # {name}")
    return result

def main():
    n, m = map(int, input().split())
    servers = []
    for _ in range(n):
        name, ip = input().split()
        servers.append((name, ip))
    commands = []
    for _ in range(m):
        commands.append(input())
    result = add_comments(commands, servers)
    for command in result:
        print(command)

if __name__ == '__main__':
    main()

