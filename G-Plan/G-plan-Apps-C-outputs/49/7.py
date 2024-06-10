
def find_matching_command(history, up_count):
    if up_count == 0:
        return history[-1]
    elif up_count <= len(history):
        return history[-up_count]
    else:
        return history[0]

def process_input(n, commands):
    history = []
    completed_commands = []
    for command in commands:
        if '^' in command:
            up_count = command.count('^')
            completed_commands.append(find_matching_command(history, up_count))
        else:
            completed_commands.append(command)
            history.append(command)
    return completed_commands

if __name__ == '__main__':
    n = int(input())
    commands = [input().strip() for _ in range(n)]
    completed_commands = process_input(n, commands)
    for command in completed_commands:
        print(command)
