
def get_input():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    return a, b, c, d

def get_splitter_ratios(a, b, c, d):
    splitter_ratios = []
    current_ratio = a / (a + b)
    next_ratio = c / (c + d)
    while current_ratio != next_ratio:
        splitter_ratios.append((current_ratio, 1 - current_ratio))
        current_ratio = next_ratio
        next_ratio = (c * current_ratio) / (c + d)
    return splitter_ratios

def get_splitter_connections(splitter_ratios):
    connections = []
    for i, (left_ratio, right_ratio) in enumerate(splitter_ratios):
        if i == 0:
            connections.append((-1, -2))
        else:
            connections.append((i - 1, i))
    return connections

def get_output(a, b, c, d):
    splitter_ratios = get_splitter_ratios(a, b, c, d)
    connections = get_splitter_connections(splitter_ratios)
    return len(splitter_ratios), connections

if __name__ == '__main__':
    a, b, c, d = get_input()
    print(get_output(a, b, c, d))

