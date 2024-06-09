
def get_new_name(name, x, y):
    new_name = ""
    for c in name:
        if c == x:
            new_name += y
        elif c == y:
            new_name += x
        else:
            new_name += c
    return new_name

def get_final_name(name, actions):
    for action in actions:
        name = get_new_name(name, action[0], action[1])
    return name

if __name__ == '__main__':
    n, m = map(int, input().split())
    name = input()
    actions = []
    for i in range(m):
        actions.append(input().split())
    print(get_final_name(name, actions))

