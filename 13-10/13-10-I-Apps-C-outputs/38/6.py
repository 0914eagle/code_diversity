
def get_leaders(n, messages):
    leaders = set()
    for message in messages:
        if message[0] == "+":
            leaders.add(int(message[1:]))
        else:
            leaders.remove(int(message[1:]))
    return leaders

def main():
    n, m = map(int, input().split())
    messages = [input() for _ in range(m)]
    leaders = get_leaders(n, messages)
    print(len(leaders))
    print(*sorted(leaders))

if __name__ == '__main__':
    main()

