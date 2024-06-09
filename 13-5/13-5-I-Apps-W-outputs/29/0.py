
def get_server_names(n, servers):
    server_names = {}
    for server in servers:
        server_names[server[1]] = server[0]
    return server_names

def add_comments(m, commands, server_names):
    result = []
    for command in commands:
        ip = command.split(" ")[1]
        result.append(f"{command} # {server_names[ip]}")
    return result

def main():
    n, m = map(int, input().split())
    servers = [input().split() for _ in range(n)]
    server_names = get_server_names(n, servers)
    commands = [input() for _ in range(m)]
    result = add_comments(m, commands, server_names)
    print("\n".join(result))

if __name__ == '__main__':
    main()

