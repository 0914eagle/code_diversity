
def get_leaders(logged_on, logged_off):
    leaders = set()
    for i in range(len(logged_on)):
        if logged_on[i] in leaders:
            leaders.remove(logged_on[i])
        leaders.add(logged_on[i])
        if logged_off[i] in leaders:
            leaders.remove(logged_off[i])
    return leaders

def main():
    n, m = map(int, input().split())
    logged_on = []
    logged_off = []
    for i in range(m):
        command, person = input().split()
        if command == '+':
            logged_on.append(int(person))
        else:
            logged_off.append(int(person))
    leaders = get_leaders(logged_on, logged_off)
    print(len(leaders))
    print(*sorted(leaders), sep=' ')

if __name__ == '__main__':
    main()

