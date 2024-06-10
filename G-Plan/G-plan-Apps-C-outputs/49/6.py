
def process_input():
    n = int(input())
    commands = []
    for _ in range(n):
        commands.append(input())
    return commands

def find_matching_command(history, up_count):
    if up_count == 0:
        return history[-1]
    return history[-up_count]

def complete_command(commands):
    history = []
    for command in commands:
        if '^' in command:
            up_count = command.count('^')
            completed_command = find_matching_command(history, up_count)
            history.append(completed_command)
        else:
            history.append(command)
    return history

if __name__ == '__main__':
    commands = process_input()
    completed_history = complete_command(commands)
    for command in completed_history:
        print(command)
