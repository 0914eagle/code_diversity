
def find_matching_command(history, up_count):
    if up_count <= len(history):
        return history[-up_count]
    return history[0]

def process_input(n, commands):
    history = []
    for command in commands:
        if '^' in command:
            up_count = command.count('^')
            completed_command = find_matching_command(history, up_count)
            print(completed_command)
            history.append(completed_command)
        else:
            print(command)
            history.append(command)

if __name__ == '__main__':
    n = int(input())
    commands = [input().strip() for _ in range(n)]
    process_input(n, commands)
