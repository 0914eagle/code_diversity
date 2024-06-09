
def get_server_names(n, server_ips):
    server_names = {}
    for i in range(n):
        name, ip = server_ips[i].split()
        server_names[ip] = name
    return server_names

def add_comments(server_names, commands):
    output = []
    for command in commands:
        ip = command.split()[1]
        name = server_names[ip]
        output.append(f"{command} # {name}")
    return output

def main():
    n, m = map(int, input().split())
    server_ips = [input() for _ in range(n)]
    commands = [input() for _ in range(m)]
    server_names = get_server_names(n, server_ips)
    output = add_comments(server_names, commands)
    print("\n".join(output))

if __name__ == '__main__':
    main()

