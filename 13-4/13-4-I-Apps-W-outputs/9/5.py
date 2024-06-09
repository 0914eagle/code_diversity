
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

def get_final_name(name, designers):
    for d in designers:
        name = get_new_name(name, d[0], d[1])
    return name

if __name__ == '__main__':
    n, m = map(int, input().split())
    name = input()
    designers = []
    for i in range(m):
        designers.append(input().split())
    print(get_final_name(name, designers))

