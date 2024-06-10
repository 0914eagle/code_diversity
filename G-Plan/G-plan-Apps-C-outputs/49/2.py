
def find_matching_command(history, up_count):
    if up_count >= len(history):
        return history[0]
    return history[-up_count]

def process_input(n, inputs):
    history = []
    for i in range(n):
        if '^' in inputs[i]:
            up_count = inputs[i].count('^')
            command = find_matching_command(history, up_count)
            print(command)
            history.append(command)
        else:
            print(inputs[i])
            history.append(inputs[i])

if __name__ == '__main__':
    n = int(input())
    inputs = [input().strip() for _ in range(n)]
    process_input(n, inputs)
