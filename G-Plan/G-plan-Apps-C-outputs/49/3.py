
def find_matching_command(history, up_count):
    if up_count == 0:
        return history[-1]
    return history[-up_count]

def process_input(n, inputs):
    history = []
    completed_commands = []
    
    for line in inputs:
        if '^' in line:
            up_count = line.count('^')
            completed_commands.append(find_matching_command(history, up_count))
        else:
            history.append(line.strip())
            completed_commands.append(line.strip())
    
    return completed_commands

if __name__ == '__main__':
    n = int(input())
    inputs = [input() for _ in range(n)]
    
    completed_commands = process_input(n, inputs)
    
    for command in completed_commands:
        print(command)
