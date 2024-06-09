
def get_server_name(ip, servers):
    for server in servers:
        if server[1] == ip:
            return server[0]
    return None

def add_server_name_to_config(config, servers):
    result = []
    for line in config:
        command, ip = line.split(" ")
        name = get_server_name(ip, servers)
        result.append(f"{command} {ip}; # {name}")
    return result

def main():
    n, m = map(int, input().split())
    servers = [input().split() for _ in range(n)]
    config = [input() for _ in range(m)]
    result = add_server_name_to_config(config, servers)
    for line in result:
        print(line)

if __name__ == '__main__':
    main()

