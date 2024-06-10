
def get_earliest_day(n, t):
    # Sort the list of days in ascending order
    t.sort()
    # The earliest day the party can be organized is the last day + 1
    return t[-1] + 1

def main():
    n = int(input())
    t = list(map(int, input().split()))
    print(get_earliest_day(n, t))

if __name__ == '__main__':
    main()

