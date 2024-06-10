
def get_entrances_and_exits(n):
    entrances = set()
    exits = set()
    for i in range(n):
        entrance, exit = map(int, input().split())
        entrances.add(entrance)
        exits.add(exit)
    return entrances, exits

def get_min_tolls(entrances, exits):
    tolls = 0
    for entrance in entrances:
        for exit in exits:
            if entrance != exit:
                tolls += abs(entrance - exit)
    return tolls

def main():
    n = int(input())
    entrances, exits = get_entrances_and_exits(n)
    print(get_min_tolls(entrances, exits))

if __name__ == '__main__':
    main()

