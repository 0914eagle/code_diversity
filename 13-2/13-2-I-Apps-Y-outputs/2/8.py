
def f1(n, k):
    # Initialize the egg holder and the list of throw commands
    egg_holder = 0
    throw_commands = []

    # Read the throw commands from stdin
    for _ in range(k):
        command = input()
        if command.isdigit():
            throw_commands.append(int(command))
        else:
            throw_commands.append(command)

    # Simulate the game
    for command in throw_commands:
        if isinstance(command, int):
            egg_holder = (egg_holder + command) % n
        else:
            for _ in range(int(command[4:])):
                egg_holder = (egg_holder - 1) % n

    return egg_holder

def f2(n, k):
    # Initialize the egg holder and the list of throw commands
    egg_holder = 0
    throw_commands = []

    # Read the throw commands from stdin
    for _ in range(k):
        command = input()
        if command.isdigit():
            throw_commands.append(int(command))
        else:
            throw_commands.append(command)

    # Simulate the game
    for command in throw_commands:
        if isinstance(command, int):
            egg_holder = (egg_holder + command) % n
        else:
            for _ in range(int(command[4:])):
                egg_holder = (egg_holder - 1) % n

    return egg_holder

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(f1(n, k))
    print(f2(n, k))

