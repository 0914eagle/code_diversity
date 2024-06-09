
def get_server_names(n, servers):
    server_names = {}
    for server in servers:
        server_names[server[1]] = server[0]
    return server_names

def add_comments(m, commands, server_names):
    output = []
    for command in commands:
        ip = command.split(" ")[1]
        name = server_names[ip]
        output.append(f"{command} # {name}")
    return output

def main():
    n, m = map(int, input().split())
    servers = [input().split() for _ in range(n)]
    server_names = get_server_names(n, servers)
    commands = [input() for _ in range(m)]
    output = add_comments(m, commands, server_names)
    print("\n".join(output))

if __name__ == '__main__':
    main()

