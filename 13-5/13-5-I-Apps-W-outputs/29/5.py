
def get_server_name(ip):
    server_names = {"192.168.0.1": "replica", "192.168.0.2": "main"}
    return server_names[ip]

def add_server_name_to_command(command, ip):
    server_name = get_server_name(ip)
    return command + " " + ip + "; #" + server_name

def main():
    n, m = map(int, input().split())
    servers = {}
    for _ in range(n):
        name, ip = input().split()
        servers[ip] = name
    commands = []
    for _ in range(m):
        command, ip = input().split()
        commands.append(add_server_name_to_command(command, ip))
    print("\n".join(commands))

if __name__ == '__main__':
    main()

