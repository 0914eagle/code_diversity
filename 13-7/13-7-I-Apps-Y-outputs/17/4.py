
def get_cycle_length(p):
    # Find the cycle length of the permutation p
    cycle_length = 0
    i = 0
    while i != p[i]:
        i = p[i]
        cycle_length += 1
    return cycle_length

def get_first_return_day(p):
    # Find the day when the book is returned to its owner for the first time
    cycle_length = get_cycle_length(p)
    return cycle_length

def get_return_day(p, i):
    # Find the day when the book of the i-th child is returned to its owner
    cycle_length = get_cycle_length(p)
    return (i - 1) % cycle_length + 1

def get_return_days(p):
    # Find the day when the book of each child is returned to its owner
    n = len(p)
    return_days = [0] * n
    for i in range(n):
        return_days[i] = get_return_day(p, i + 1)
    return return_days

def main():
    queries = int(input())
    for _ in range(queries):
        n = int(input())
        p = list(map(int, input().split()))
        return_days = get_return_days(p)
        print(*return_days)

if __name__ == '__main__':
    main()

