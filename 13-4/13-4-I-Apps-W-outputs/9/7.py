
def get_new_name(name, x, y):
    new_name = ""
    for char in name:
        if char == x:
            new_name += y
        elif char == y:
            new_name += x
        else:
            new_name += char
    return new_name

def get_final_name(name, designers):
    for designer in designers:
        name = get_new_name(name, designer[0], designer[1])
    return name

if __name__ == '__main__':
    n, m = map(int, input().split())
    name = input()
    designers = []
    for _ in range(m):
        designers.append(input().split())
    print(get_final_name(name, designers))

