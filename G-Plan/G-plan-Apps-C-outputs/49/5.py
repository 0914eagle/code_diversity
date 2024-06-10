
def complete_command_history(n, commands):
    history = []
    for command in commands:
        if '^' in command:
            count = command.count('^')
            if count <= len(history):
                command = history[-count]
        history.append(command.replace('^', ''))
        print(history[-1])

if __name__ == '__main__':
    n = int(input())
    commands = [input().strip() for _ in range(n)]
    complete_command_history(n, commands)
