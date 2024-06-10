
def get_leaders(n, m, logs):
    leaders = set()
    for log in logs:
        if log[0] == '+':
            leaders.add(log[1])
        else:
            leaders.remove(log[1])
    
    return leaders

def main():
    n, m = map(int, input().split())
    logs = [input().split() for _ in range(m)]
    leaders = get_leaders(n, m, logs)
    print(len(leaders))
    print(*sorted(leaders), sep=' ')

if __name__ == '__main__':
    main()

