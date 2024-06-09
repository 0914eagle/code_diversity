
def get_new_name(name, designers):
    for designer in designers:
        x, y = designer
        name = name.replace(x, y)
        name = name.replace(y, x)
    return name

def main():
    n, m = map(int, input().split())
    name = input()
    designers = []
    for i in range(m):
        x, y = input().split()
        designers.append((x, y))
    print(get_new_name(name, designers))

if __name__ == '__main__':
    main()

