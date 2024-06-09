
def get_server_names(n):
    server_names = {}
    for i in range(n):
        name, ip = input().split()
        server_names[ip] = name
    return server_names

def add_comments(server_names, commands):
    for command in commands:
        ip = command.split()[1]
        name = server_names[ip]
        command += " #" + name
    return commands

def main():
    n, m = map(int, input().split())
    server_names = get_server_names(n)
    commands = []
    for i in range(m):
        commands.append(input())
    commands = add_comments(server_names, commands)
    for command in commands:
        print(command)

if __name__ == '__main__':
    main()

