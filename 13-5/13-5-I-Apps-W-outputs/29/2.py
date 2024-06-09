
def get_server_info(n, m):
    servers = {}
    for _ in range(n):
        name, ip = input().split()
        servers[ip] = name
    return servers

def add_server_names(servers, commands):
    for command in commands:
        ip = command.split()[1]
        name = servers[ip]
        command += f" # {name}"
    return commands

def main():
    n, m = map(int, input().split())
    servers = get_server_info(n, m)
    commands = [input() for _ in range(m)]
    commands = add_server_names(servers, commands)
    for command in commands:
        print(command)

if __name__ == '__main__':
    main()

