
def find_matching_command(history, up_count):
    if up_count == 0:
        return history[-1]
    elif up_count <= len(history):
        return history[-up_count]
    else:
        return history[0]

def process_input(n):
    history = []
    for _ in range(n):
        line = input().strip()
        if '^' in line:
            up_count = line.count('^')
            completed_command = find_matching_command(history, up_count)
            print(completed_command)
            history.append(completed_command)
        else:
            print(line)
            history.append(line)

if __name__ == '__main__':
    n = int(input())
    process_input(n)
